--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1
-- Dumped by pg_dump version 15.0 (Ubuntu 15.0-1.pgdg22.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO postgres;

--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: feeding; Type: TABLE; Schema: public; Owner: postgres_temporary_object_holder
--

CREATE TABLE public.feeding (
    x_var smallint,
    notes text,
    b_m1 text,
    b_m2 text,
    b_m3 text,
    b_m4 text,
    b_m5 text,
    b_sl integer,
    b_pl integer,
    l_m1 text,
    l_m2 text,
    l_m3 text,
    l_m4 text,
    l_m5 text,
    l_sl integer,
    l_pl integer,
    d_m1 text,
    d_m2 text,
    d_m3 text,
    d_m4 text,
    d_m5 text,
    d_sl integer,
    d_pl integer,
    s_level integer,
    sleep integer,
    rest integer,
    date text,
    id integer NOT NULL
);


ALTER TABLE public.feeding OWNER TO postgres_temporary_object_holder;

--
-- Name: TABLE feeding; Type: COMMENT; Schema: public; Owner: postgres_temporary_object_holder
--

COMMENT ON TABLE public.feeding IS 'feeding register';


--
-- Name: COLUMN feeding.b_m1; Type: COMMENT; Schema: public; Owner: postgres_temporary_object_holder
--

COMMENT ON COLUMN public.feeding.b_m1 IS 'Breakfast meat 1';


--
-- Name: COLUMN feeding.b_m2; Type: COMMENT; Schema: public; Owner: postgres_temporary_object_holder
--

COMMENT ON COLUMN public.feeding.b_m2 IS 'Breakfast meat 2';


--
-- Name: feeding_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres_temporary_object_holder
--

CREATE SEQUENCE public.feeding_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.feeding_id_seq OWNER TO postgres_temporary_object_holder;

--
-- Name: feeding_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres_temporary_object_holder
--

ALTER SEQUENCE public.feeding_id_seq OWNED BY public.feeding.id;


--
-- Name: feeding id; Type: DEFAULT; Schema: public; Owner: postgres_temporary_object_holder
--

ALTER TABLE ONLY public.feeding ALTER COLUMN id SET DEFAULT nextval('public.feeding_id_seq'::regclass);


--
-- Data for Name: feeding; Type: TABLE DATA; Schema: public; Owner: postgres_temporary_object_holder
--

-- Manually DELETED!

--
-- Name: feeding_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres_temporary_object_holder
--

SELECT pg_catalog.setval('public.feeding_id_seq', 26, true);


--
-- Name: feeding feeding_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres_temporary_object_holder
--

ALTER TABLE ONLY public.feeding
    ADD CONSTRAINT feeding_pkey PRIMARY KEY (id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;
GRANT USAGE ON SCHEMA public TO anon;
GRANT USAGE ON SCHEMA public TO authenticated;
GRANT USAGE ON SCHEMA public TO service_role;


--
-- Name: TABLE feeding; Type: ACL; Schema: public; Owner: postgres_temporary_object_holder
--

GRANT ALL ON TABLE public.feeding TO postgres;
GRANT ALL ON TABLE public.feeding TO anon;
GRANT ALL ON TABLE public.feeding TO authenticated;
GRANT ALL ON TABLE public.feeding TO service_role;


--
-- Name: SEQUENCE feeding_id_seq; Type: ACL; Schema: public; Owner: postgres_temporary_object_holder
--

GRANT ALL ON SEQUENCE public.feeding_id_seq TO postgres;
GRANT ALL ON SEQUENCE public.feeding_id_seq TO anon;
GRANT ALL ON SEQUENCE public.feeding_id_seq TO authenticated;
GRANT ALL ON SEQUENCE public.feeding_id_seq TO service_role;


--
-- Name: DEFAULT PRIVILEGES FOR SEQUENCES; Type: DEFAULT ACL; Schema: public; Owner: postgres
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON SEQUENCES  TO postgres;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON SEQUENCES  TO anon;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON SEQUENCES  TO authenticated;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON SEQUENCES  TO service_role;


--
-- Name: DEFAULT PRIVILEGES FOR SEQUENCES; Type: DEFAULT ACL; Schema: public; Owner: supabase_admin
--

ALTER DEFAULT PRIVILEGES FOR ROLE supabase_admin IN SCHEMA public GRANT ALL ON SEQUENCES  TO postgres;
ALTER DEFAULT PRIVILEGES FOR ROLE supabase_admin IN SCHEMA public GRANT ALL ON SEQUENCES  TO anon;
ALTER DEFAULT PRIVILEGES FOR ROLE supabase_admin IN SCHEMA public GRANT ALL ON SEQUENCES  TO authenticated;
ALTER DEFAULT PRIVILEGES FOR ROLE supabase_admin IN SCHEMA public GRANT ALL ON SEQUENCES  TO service_role;


--
-- Name: DEFAULT PRIVILEGES FOR SEQUENCES; Type: DEFAULT ACL; Schema: public; Owner: postgres_temporary_object_holder
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres_temporary_object_holder IN SCHEMA public GRANT ALL ON SEQUENCES  TO postgres;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres_temporary_object_holder IN SCHEMA public GRANT ALL ON SEQUENCES  TO anon;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres_temporary_object_holder IN SCHEMA public GRANT ALL ON SEQUENCES  TO authenticated;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres_temporary_object_holder IN SCHEMA public GRANT ALL ON SEQUENCES  TO service_role;


--
-- Name: DEFAULT PRIVILEGES FOR TYPES; Type: DEFAULT ACL; Schema: public; Owner: postgres_temporary_object_holder
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres_temporary_object_holder IN SCHEMA public GRANT ALL ON TYPES  TO postgres;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres_temporary_object_holder IN SCHEMA public GRANT ALL ON TYPES  TO anon;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres_temporary_object_holder IN SCHEMA public GRANT ALL ON TYPES  TO authenticated;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres_temporary_object_holder IN SCHEMA public GRANT ALL ON TYPES  TO service_role;


--
-- Name: DEFAULT PRIVILEGES FOR FUNCTIONS; Type: DEFAULT ACL; Schema: public; Owner: postgres
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON FUNCTIONS  TO postgres;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON FUNCTIONS  TO anon;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON FUNCTIONS  TO authenticated;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON FUNCTIONS  TO service_role;


--
-- Name: DEFAULT PRIVILEGES FOR FUNCTIONS; Type: DEFAULT ACL; Schema: public; Owner: supabase_admin
--

ALTER DEFAULT PRIVILEGES FOR ROLE supabase_admin IN SCHEMA public GRANT ALL ON FUNCTIONS  TO postgres;
ALTER DEFAULT PRIVILEGES FOR ROLE supabase_admin IN SCHEMA public GRANT ALL ON FUNCTIONS  TO anon;
ALTER DEFAULT PRIVILEGES FOR ROLE supabase_admin IN SCHEMA public GRANT ALL ON FUNCTIONS  TO authenticated;
ALTER DEFAULT PRIVILEGES FOR ROLE supabase_admin IN SCHEMA public GRANT ALL ON FUNCTIONS  TO service_role;


--
-- Name: DEFAULT PRIVILEGES FOR FUNCTIONS; Type: DEFAULT ACL; Schema: public; Owner: postgres_temporary_object_holder
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres_temporary_object_holder IN SCHEMA public GRANT ALL ON FUNCTIONS  TO postgres;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres_temporary_object_holder IN SCHEMA public GRANT ALL ON FUNCTIONS  TO anon;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres_temporary_object_holder IN SCHEMA public GRANT ALL ON FUNCTIONS  TO authenticated;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres_temporary_object_holder IN SCHEMA public GRANT ALL ON FUNCTIONS  TO service_role;


--
-- Name: DEFAULT PRIVILEGES FOR TABLES; Type: DEFAULT ACL; Schema: public; Owner: postgres
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON TABLES  TO postgres;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON TABLES  TO anon;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON TABLES  TO authenticated;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON TABLES  TO service_role;


--
-- Name: DEFAULT PRIVILEGES FOR TABLES; Type: DEFAULT ACL; Schema: public; Owner: supabase_admin
--

ALTER DEFAULT PRIVILEGES FOR ROLE supabase_admin IN SCHEMA public GRANT ALL ON TABLES  TO postgres;
ALTER DEFAULT PRIVILEGES FOR ROLE supabase_admin IN SCHEMA public GRANT ALL ON TABLES  TO anon;
ALTER DEFAULT PRIVILEGES FOR ROLE supabase_admin IN SCHEMA public GRANT ALL ON TABLES  TO authenticated;
ALTER DEFAULT PRIVILEGES FOR ROLE supabase_admin IN SCHEMA public GRANT ALL ON TABLES  TO service_role;


--
-- Name: DEFAULT PRIVILEGES FOR TABLES; Type: DEFAULT ACL; Schema: public; Owner: postgres_temporary_object_holder
--

ALTER DEFAULT PRIVILEGES FOR ROLE postgres_temporary_object_holder IN SCHEMA public GRANT ALL ON TABLES  TO postgres;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres_temporary_object_holder IN SCHEMA public GRANT ALL ON TABLES  TO anon;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres_temporary_object_holder IN SCHEMA public GRANT ALL ON TABLES  TO authenticated;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres_temporary_object_holder IN SCHEMA public GRANT ALL ON TABLES  TO service_role;


--
-- PostgreSQL database dump complete
--

