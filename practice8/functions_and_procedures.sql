-- 1. Base Table
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50),
    phone VARCHAR(20) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Function: Pattern Matching Search
CREATE OR REPLACE FUNCTION search_contacts(search_pattern TEXT)
RETURNS TABLE(id INT, username VARCHAR, first_name VARCHAR, last_name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.username, p.first_name, p.last_name, p.phone
    FROM phonebook p
    WHERE p.first_name ILIKE '%' || search_pattern || '%'
       OR p.last_name ILIKE '%' || search_pattern || '%'
       OR p.phone LIKE '%' || search_pattern || '%';
END;
$$ LANGUAGE plpgsql;

-- 3. Procedure: Upsert a User (Insert or Update Phone)
CREATE OR REPLACE PROCEDURE upsert_contact(
    p_username VARCHAR,
    p_first_name VARCHAR,
    p_last_name VARCHAR,
    p_phone VARCHAR
) AS $$
BEGIN
    INSERT INTO phonebook (username, first_name, last_name, phone)
    VALUES (p_username, p_first_name, p_last_name, p_phone)
    ON CONFLICT (username) 
    DO UPDATE SET phone = EXCLUDED.phone;
END;
$$ LANGUAGE plpgsql;

-- 4. Procedure: Bulk Insert with Loop, IF validation, and Return Incorrect Data
-- Note: PostgreSQL procedures pass data back via INOUT or OUT parameters.
CREATE OR REPLACE PROCEDURE bulk_insert_with_validation(
    IN p_usernames VARCHAR[],
    IN p_first_names VARCHAR[],
    IN p_last_names VARCHAR[],
    IN p_phones VARCHAR[],
    OUT bad_usernames VARCHAR[],
    OUT bad_phones VARCHAR[],
    OUT error_reasons TEXT[]
) AS $$
DECLARE
    i INT;
    v_username VARCHAR;
    v_first_name VARCHAR;
    v_last_name VARCHAR;
    v_phone VARCHAR;
BEGIN
    -- Initialize arrays
    bad_usernames := '{}';
    bad_phones := '{}';
    error_reasons := '{}';

    -- Loop through the array indices
    FOR i IN 1 .. array_length(p_usernames, 1) LOOP
        v_username := p_usernames[i];
        v_first_name := p_first_names[i];
        v_last_name := p_last_names[i];
        v_phone := p_phones[i];

        -- Basic structural validation: Phone must start with '+' and be between 7-15 digits
        IF v_phone NOT SIMILAR TO '\+[0-9]{7,15}' THEN
            bad_usernames := array_append(bad_usernames, v_username);
            bad_phones := array_append(bad_phones, v_phone);
            error_reasons := array_append(error_reasons, 'Invalid phone format (Must be + followed by 7-15 digits)');
        
        -- Check if phone already belongs to someone else to avoid unique constraint crash
        ELSIF EXISTS (SELECT 1 FROM phonebook WHERE phone = v_phone AND username != v_username) THEN
            bad_usernames := array_append(bad_usernames, v_username);
            bad_phones := array_append(bad_phones, v_phone);
            error_reasons := array_append(error_reasons, 'Phone number already assigned to another user');
            
        ELSE
            -- Safe to insert or update
            INSERT INTO phonebook (username, first_name, last_name, phone)
            VALUES (v_username, v_first_name, v_last_name, v_phone)
            ON CONFLICT (username) DO UPDATE SET phone = EXCLUDED.phone;
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

-- 5. Function: Pagination Setup
CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(username VARCHAR, first_name VARCHAR, last_name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT p.username, p.first_name, p.last_name, p.phone
    FROM phonebook p
    ORDER BY p.id ASC
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;

-- 6. Procedure: Dynamic Delete
CREATE OR REPLACE PROCEDURE delete_contact_by_identifier(
    p_identifier VARCHAR,
    p_strategy VARCHAR -- Must be either 'username' or 'phone'
) AS $$
BEGIN
    IF p_strategy = 'username' THEN
        DELETE FROM phonebook WHERE username = p_identifier;
    ELSIF p_strategy = 'phone' THEN
        DELETE FROM phonebook WHERE phone = p_identifier;
    ELSE
        RAISE EXCEPTION 'Invalid strategy profile. Use "username" or "phone".';
    END IF;
END;
$$ LANGUAGE plpgsql;