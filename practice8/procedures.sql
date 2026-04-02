-- UPSERT
CREATE OR REPLACE PROCEDURE upsert_contact(
    p_first_name VARCHAR,
    p_last_name VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE phone = p_phone) THEN
        UPDATE contacts
        SET first_name = p_first_name,
            last_name = p_last_name
        WHERE phone = p_phone;
    ELSE
        INSERT INTO contacts(first_name, last_name, phone)
        VALUES (p_first_name, p_last_name, p_phone);
    END IF;
END;
$$;


-- BULK INSERT 
CREATE OR REPLACE PROCEDURE insert_many_contacts(p_data TEXT[])
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
    v_first VARCHAR;
    v_last  VARCHAR;
    v_phone VARCHAR;
    v_entry TEXT;
    invalid_list TEXT := '';
BEGIN
    FOR i IN 1..array_length(p_data, 1) LOOP
        v_entry := p_data[i];
        v_first := split_part(v_entry, '|', 1);
        v_last  := split_part(v_entry, '|', 2);
        v_phone := split_part(v_entry, '|', 3);

        IF v_phone !~ '^\+?[0-9]{7,15}$' THEN
            invalid_list := invalid_list || v_first || ' ' || v_last || ' - ' || v_phone || E'\n';
        ELSE
            CALL upsert_contact(v_first, v_last, v_phone);
        END IF;
    END LOOP;

    IF invalid_list <> '' THEN
        RAISE NOTICE 'Invalid entries:%', E'\n' || invalid_list;
    END IF;
END;
$$;


--DELETE
CREATE OR REPLACE PROCEDURE delete_contact_proc(p_value VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts
    WHERE first_name = p_value
       OR last_name = p_value
       OR phone = p_value;
END;
$$;