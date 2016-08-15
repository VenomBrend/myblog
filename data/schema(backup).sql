drop table if exists entries;
create table entries (
    id integer primary key autoincrement,
    slug text not null,
    title text not null,
    short_text text not null,
    full_text text not null,
    timestamp text not null
);
