CREATE TABLE public.imported_users (
	id varchar NOT NULL,
	"name" varchar NULL,
	login varchar NULL,
	priority int4 NULL DEFAULT 3,
	CONSTRAINT imported_users_pkey PRIMARY KEY (id)
);

-- Permissions

ALTER TABLE public.imported_users OWNER TO postgres;
GRANT ALL ON TABLE public.imported_users TO postgres;

CREATE TABLE public.priority1 (
	id varchar NOT NULL,
	CONSTRAINT priority1_pkey PRIMARY KEY (id)
);

-- Permissions

ALTER TABLE public.priority1 OWNER TO postgres;
GRANT ALL ON TABLE public.priority1 TO postgres;

CREATE TABLE public.priority2 (
        id varchar NOT NULL,
        CONSTRAINT priority2_pkey PRIMARY KEY (id)
);

-- Permissions

ALTER TABLE public.priority2 OWNER TO postgres;
GRANT ALL ON TABLE public.priority2 TO postgres;

-- insensitive case ON

CREATE EXTENSION citext;
ALTER TABLE public.imported_users ALTER COLUMN name TYPE citext;
ALTER TABLE public.imported_users ALTER COLUMN login TYPE citext;

--CREATE INDEX idx_name_imported_users ON imported_users (name);
--CREATE INDEX idx_login_imported_users ON imported_users (login);

\timing on

-- imports

COPY public.imported_users (id,name,login)
FROM '/tmp/users.csv'
WITH (format csv, header);

COPY public.priority1
FROM '/tmp/lista_relevancia_1.txt'
WITH (format csv, header);

COPY public.priority2
FROM '/tmp/lista_relevancia_2.txt'
WITH (format csv, header);

-- updates

update public.imported_users set priority = 1 where id in (select id from priority1);
update public.imported_users set priority = 2 where id in (select id from priority2);
