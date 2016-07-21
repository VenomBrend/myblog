drop table if exists entries;
create table entries (
    id integer primary key autoincrement,
    slug text,
    title text,
    short_text text,
    full_text text,
    timestamp text
);
