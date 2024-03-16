DROP TABLE IF EXISTS Users;
CREATE TABLE IF NOT EXISTS Users(
    `id` VARCHAR(256) primary KEY,
    `username` VARCHAR(32) NOT NULL,
    `email` VARCHAR(100) NOT NULL UNIQUE,
    `password` TEXT NOT NULL,
    `created` TIMESTAMP DEFAULT now(),
    `updated` TIMESTAMP DEFAULT now()
)