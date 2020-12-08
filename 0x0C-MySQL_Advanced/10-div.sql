-- safe divide
DELIMITER //

CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT
BEGIN
    DECLARE ret FLOAT;
    IF b = 0 THEN
        SET ret = 0;
    ELSE
        SET ret = a / b;
    END IF;
    RETURN ret;
END //
