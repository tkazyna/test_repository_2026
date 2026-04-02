-- SHOW ALL CONTACTS
CREATE OR REPLACE FUNCTION get_all_contacts()
RETURNS TABLE(id INT, first_name VARCHAR, last_name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.first_name, c.last_name, c.phone
    FROM contacts c
    ORDER BY c.id;
END;
$$ LANGUAGE plpgsql;


-- SEARCH FUNCTION
CREATE OR REPLACE FUNCTION search_contacts(p text)
RETURNS TABLE(id INT, first_name VARCHAR, last_name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.first_name, c.last_name, c.phone FROM contacts c
    WHERE c.first_name ILIKE '%' || p || '%'
       OR c.last_name ILIKE '%' || p || '%'
       OR c.phone ILIKE '%' || p || '%';
END;
$$ LANGUAGE plpgsql;


-- PAGINATION FUNCTION
CREATE OR REPLACE FUNCTION get_contacts_paginated(lim INT, off INT)
RETURNS TABLE(id INT, first_name VARCHAR, last_name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.first_name, c.last_name, c.phone FROM contacts c
    ORDER BY c.id
    LIMIT lim OFFSET off;
END;
$$ LANGUAGE plpgsql;