--
-- PostgreSQL database dump
--

-- Dumped from database version 10.10 (Ubuntu 10.10-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.10 (Ubuntu 10.10-0ubuntu0.18.04.1)

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
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: companies; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.companies (
    company_id integer NOT NULL,
    name character varying(64) NOT NULL,
    company_type character varying(64) NOT NULL
);


ALTER TABLE public.companies OWNER TO vagrant;

--
-- Name: companies_company_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.companies_company_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.companies_company_id_seq OWNER TO vagrant;

--
-- Name: companies_company_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.companies_company_id_seq OWNED BY public.companies.company_id;


--
-- Name: consumptions; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.consumptions (
    consumption_id integer NOT NULL,
    utility integer,
    year character varying(10) NOT NULL,
    consumed integer NOT NULL
);


ALTER TABLE public.consumptions OWNER TO vagrant;

--
-- Name: consumptions_consumption_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.consumptions_consumption_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.consumptions_consumption_id_seq OWNER TO vagrant;

--
-- Name: consumptions_consumption_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.consumptions_consumption_id_seq OWNED BY public.consumptions.consumption_id;


--
-- Name: productions; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.productions (
    production_id integer NOT NULL,
    application_id character varying(25),
    energy_type character varying(64) NOT NULL,
    start_date timestamp without time zone NOT NULL,
    end_date timestamp without time zone NOT NULL,
    produced integer NOT NULL
);


ALTER TABLE public.productions OWNER TO vagrant;

--
-- Name: productions_production_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.productions_production_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.productions_production_id_seq OWNER TO vagrant;

--
-- Name: productions_production_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.productions_production_id_seq OWNED BY public.productions.production_id;


--
-- Name: programs; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.programs (
    application_id character varying(25) NOT NULL,
    admin integer,
    city character varying(64) NOT NULL,
    county character varying(64) NOT NULL,
    zipcode character varying(5) NOT NULL,
    contractor integer,
    pv_manuf integer,
    invert_manuf integer,
    status character varying(64)
);


ALTER TABLE public.programs OWNER TO vagrant;

--
-- Name: companies company_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.companies ALTER COLUMN company_id SET DEFAULT nextval('public.companies_company_id_seq'::regclass);


--
-- Name: consumptions consumption_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.consumptions ALTER COLUMN consumption_id SET DEFAULT nextval('public.consumptions_consumption_id_seq'::regclass);


--
-- Name: productions production_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.productions ALTER COLUMN production_id SET DEFAULT nextval('public.productions_production_id_seq'::regclass);


--
-- Data for Name: companies; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.companies (company_id, name, company_type) FROM stdin;
1	Pacific Gas and Electric	energy utility
2	Southern California Edison Company	energy utility
3	San Diego Gas and Electric Company	energy utility
4	SPG Solar	solar contractor
5	Kyocera Solar	photovoltaics manufacturer
6	Xantrex Technology	inverter manufacturer
\.


--
-- Data for Name: consumptions; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.consumptions (consumption_id, utility, year, consumed) FROM stdin;
\.


--
-- Data for Name: productions; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.productions (production_id, application_id, energy_type, start_date, end_date, produced) FROM stdin;
1	SD-CSI-00001	solar	2007-05-01 00:00:00	2007-05-31 00:00:00	36578
\.


--
-- Data for Name: programs; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.programs (application_id, admin, city, county, zipcode, contractor, pv_manuf, invert_manuf, status) FROM stdin;
SD-CSI-00001	3	San Diego	San Diego	92121	4	5	6	\N
\.


--
-- Name: companies_company_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.companies_company_id_seq', 6, true);


--
-- Name: consumptions_consumption_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.consumptions_consumption_id_seq', 1, false);


--
-- Name: productions_production_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.productions_production_id_seq', 1, true);


--
-- Name: companies companies_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.companies
    ADD CONSTRAINT companies_pkey PRIMARY KEY (company_id);


--
-- Name: consumptions consumptions_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.consumptions
    ADD CONSTRAINT consumptions_pkey PRIMARY KEY (consumption_id);


--
-- Name: productions productions_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.productions
    ADD CONSTRAINT productions_pkey PRIMARY KEY (production_id);


--
-- Name: programs programs_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.programs
    ADD CONSTRAINT programs_pkey PRIMARY KEY (application_id);


--
-- Name: consumptions consumptions_utility_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.consumptions
    ADD CONSTRAINT consumptions_utility_fkey FOREIGN KEY (utility) REFERENCES public.companies(company_id);


--
-- Name: productions productions_application_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.productions
    ADD CONSTRAINT productions_application_id_fkey FOREIGN KEY (application_id) REFERENCES public.programs(application_id);


--
-- Name: programs programs_admin_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.programs
    ADD CONSTRAINT programs_admin_fkey FOREIGN KEY (admin) REFERENCES public.companies(company_id);


--
-- Name: programs programs_contractor_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.programs
    ADD CONSTRAINT programs_contractor_fkey FOREIGN KEY (contractor) REFERENCES public.companies(company_id);


--
-- Name: programs programs_invert_manuf_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.programs
    ADD CONSTRAINT programs_invert_manuf_fkey FOREIGN KEY (invert_manuf) REFERENCES public.companies(company_id);


--
-- Name: programs programs_pv_manuf_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.programs
    ADD CONSTRAINT programs_pv_manuf_fkey FOREIGN KEY (pv_manuf) REFERENCES public.companies(company_id);


--
-- PostgreSQL database dump complete
--

