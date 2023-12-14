--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0
-- Dumped by pg_dump version 16.0

-- Started on 2023-11-16 03:05:25

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
-- TOC entry 5 (class 2615 OID 16447)
-- Name: hotel_schema; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA hotel_schema;


ALTER SCHEMA hotel_schema OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 216 (class 1259 OID 16462)
-- Name: booking; Type: TABLE; Schema: hotel_schema; Owner: postgres
--

CREATE TABLE hotel_schema.booking (
    booking_id bigint NOT NULL,
    visitor_id bigint NOT NULL,
    room_id numeric NOT NULL,
    settle_datetime date NOT NULL,
    eviction_datetime date NOT NULL
);


ALTER TABLE hotel_schema.booking OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16469)
-- Name: booking_booking_id_seq; Type: SEQUENCE; Schema: hotel_schema; Owner: postgres
--

ALTER TABLE hotel_schema.booking ALTER COLUMN booking_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME hotel_schema.booking_booking_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 215 (class 1259 OID 16455)
-- Name: room; Type: TABLE; Schema: hotel_schema; Owner: postgres
--

CREATE TABLE hotel_schema.room (
    room_id numeric NOT NULL,
    type text NOT NULL,
    floor numeric NOT NULL,
    price numeric NOT NULL
);


ALTER TABLE hotel_schema.room OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 16516)
-- Name: schedule; Type: TABLE; Schema: hotel_schema; Owner: postgres
--

CREATE TABLE hotel_schema.schedule (
    schedule_id bigint NOT NULL,
    task_id bigint NOT NULL,
    staff_id bigint NOT NULL,
    room_id numeric NOT NULL,
    date timestamp without time zone NOT NULL,
    date_end timestamp without time zone,
    ordered boolean NOT NULL
);


ALTER TABLE hotel_schema.schedule OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 16515)
-- Name: schedule_schedule_id_seq; Type: SEQUENCE; Schema: hotel_schema; Owner: postgres
--

ALTER TABLE hotel_schema.schedule ALTER COLUMN schedule_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME hotel_schema.schedule_schedule_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 221 (class 1259 OID 16500)
-- Name: staff; Type: TABLE; Schema: hotel_schema; Owner: postgres
--

CREATE TABLE hotel_schema.staff (
    staff_id bigint NOT NULL,
    name text NOT NULL,
    surname text NOT NULL,
    patronymic text NOT NULL,
    passport numeric(10,0) NOT NULL,
    experience numeric NOT NULL,
    salary numeric NOT NULL
);


ALTER TABLE hotel_schema.staff OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 16499)
-- Name: staff_staff_id_seq; Type: SEQUENCE; Schema: hotel_schema; Owner: postgres
--

ALTER TABLE hotel_schema.staff ALTER COLUMN staff_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME hotel_schema.staff_staff_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 223 (class 1259 OID 16508)
-- Name: task; Type: TABLE; Schema: hotel_schema; Owner: postgres
--

CREATE TABLE hotel_schema.task (
    task_id bigint NOT NULL,
    name text NOT NULL,
    duration numeric NOT NULL,
    payment numeric NOT NULL
);


ALTER TABLE hotel_schema.task OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 16507)
-- Name: task_task_id_seq; Type: SEQUENCE; Schema: hotel_schema; Owner: postgres
--

ALTER TABLE hotel_schema.task ALTER COLUMN task_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME hotel_schema.task_task_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 218 (class 1259 OID 16480)
-- Name: visitor; Type: TABLE; Schema: hotel_schema; Owner: postgres
--

CREATE TABLE hotel_schema.visitor (
    visitor_id bigint NOT NULL,
    name text NOT NULL,
    surname text NOT NULL,
    patronymic text NOT NULL,
    passport numeric(10,0) NOT NULL,
    phone_number text NOT NULL,
    gender text NOT NULL
);


ALTER TABLE hotel_schema.visitor OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16487)
-- Name: visitor_visitor_id_seq; Type: SEQUENCE; Schema: hotel_schema; Owner: postgres
--

ALTER TABLE hotel_schema.visitor ALTER COLUMN visitor_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME hotel_schema.visitor_visitor_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 4873 (class 0 OID 16462)
-- Dependencies: 216
-- Data for Name: booking; Type: TABLE DATA; Schema: hotel_schema; Owner: postgres
--

INSERT INTO hotel_schema.booking (booking_id, visitor_id, room_id, settle_datetime, eviction_datetime) OVERRIDING SYSTEM VALUE VALUES (1, 4, 301, '2023-09-06 12:00:00+03', '2023-09-09 12:00:00+03');
INSERT INTO hotel_schema.booking (booking_id, visitor_id, room_id, settle_datetime, eviction_datetime) OVERRIDING SYSTEM VALUE VALUES (2, 3, 303, '2023-09-13 12:00:00+03', '2023-09-15 12:00:00+03');
INSERT INTO hotel_schema.booking (booking_id, visitor_id, room_id, settle_datetime, eviction_datetime) OVERRIDING SYSTEM VALUE VALUES (3, 10, 303, '2023-09-18 12:00:00+03', '2023-09-19 12:00:00+03');
INSERT INTO hotel_schema.booking (booking_id, visitor_id, room_id, settle_datetime, eviction_datetime) OVERRIDING SYSTEM VALUE VALUES (4, 6, 103, '2023-09-22 12:00:00+03', '2023-09-25 12:00:00+03');
INSERT INTO hotel_schema.booking (booking_id, visitor_id, room_id, settle_datetime, eviction_datetime) OVERRIDING SYSTEM VALUE VALUES (6, 5, 202, '2023-10-07 12:00:00+03', '2023-10-09 12:00:00+03');
INSERT INTO hotel_schema.booking (booking_id, visitor_id, room_id, settle_datetime, eviction_datetime) OVERRIDING SYSTEM VALUE VALUES (7, 1, 102, '2023-10-09 12:00:00+03', '2023-10-10 12:00:00+03');
INSERT INTO hotel_schema.booking (booking_id, visitor_id, room_id, settle_datetime, eviction_datetime) OVERRIDING SYSTEM VALUE VALUES (8, 1, 401, '2023-10-18 12:00:00+03', '2023-10-20 12:00:00+03');
INSERT INTO hotel_schema.booking (booking_id, visitor_id, room_id, settle_datetime, eviction_datetime) OVERRIDING SYSTEM VALUE VALUES (9, 2, 303, '2023-10-21 12:00:00+03', '2023-10-22 12:00:00+03');
INSERT INTO hotel_schema.booking (booking_id, visitor_id, room_id, settle_datetime, eviction_datetime) OVERRIDING SYSTEM VALUE VALUES (10, 3, 401, '2023-10-26 12:00:00+03', '2023-10-28 12:00:00+03');
INSERT INTO hotel_schema.booking (booking_id, visitor_id, room_id, settle_datetime, eviction_datetime) OVERRIDING SYSTEM VALUE VALUES (5, 9, 302, '2023-10-03 12:00:00+03', '2023-10-07 12:00:00+03');


--
-- TOC entry 4872 (class 0 OID 16455)
-- Dependencies: 215
-- Data for Name: room; Type: TABLE DATA; Schema: hotel_schema; Owner: postgres
--

INSERT INTO hotel_schema.room (room_id, type, floor, price) VALUES (401, 'lux', 4, 4200);
INSERT INTO hotel_schema.room (room_id, type, floor, price) VALUES (303, 'comfort', 3, 3500);
INSERT INTO hotel_schema.room (room_id, type, floor, price) VALUES (302, 'comfort', 3, 3500);
INSERT INTO hotel_schema.room (room_id, type, floor, price) VALUES (301, 'comfort', 3, 3500);
INSERT INTO hotel_schema.room (room_id, type, floor, price) VALUES (203, 'classic', 2, 2700);
INSERT INTO hotel_schema.room (room_id, type, floor, price) VALUES (202, 'classic', 2, 2700);
INSERT INTO hotel_schema.room (room_id, type, floor, price) VALUES (201, 'classic', 2, 2700);
INSERT INTO hotel_schema.room (room_id, type, floor, price) VALUES (103, 'classic', 1, 2200);
INSERT INTO hotel_schema.room (room_id, type, floor, price) VALUES (102, 'classic', 1, 2200);
INSERT INTO hotel_schema.room (room_id, type, floor, price) VALUES (101, 'classic', 1, 2200);


--
-- TOC entry 4882 (class 0 OID 16516)
-- Dependencies: 225
-- Data for Name: schedule; Type: TABLE DATA; Schema: hotel_schema; Owner: postgres
--

INSERT INTO hotel_schema.schedule (schedule_id, task_id, staff_id, room_id, date, date_end, ordered) OVERRIDING SYSTEM VALUE VALUES (1, 6, 9, 301, '2023-09-07 20:00:00+03', '2023-09-07 20:27:00+03', true);
INSERT INTO hotel_schema.schedule (schedule_id, task_id, staff_id, room_id, date, date_end, ordered) OVERRIDING SYSTEM VALUE VALUES (2, 1, 8, 301, '2023-09-09 12:00:00+03', '2023-09-09 13:00:00+03', false);
INSERT INTO hotel_schema.schedule (schedule_id, task_id, staff_id, room_id, date, date_end, ordered) OVERRIDING SYSTEM VALUE VALUES (3, 1, 3, 303, '2023-09-15 12:00:00+03', '2023-09-15 13:12:00+03', false);
INSERT INTO hotel_schema.schedule (schedule_id, task_id, staff_id, room_id, date, date_end, ordered) OVERRIDING SYSTEM VALUE VALUES (4, 1, 4, 303, '2023-09-19 12:00:00+03', '2023-09-19 13:00:00+03', false);
INSERT INTO hotel_schema.schedule (schedule_id, task_id, staff_id, room_id, date, date_end, ordered) OVERRIDING SYSTEM VALUE VALUES (5, 4, 1, 103, '2023-09-24 14:00:00+03', '2023-09-24 15:00:00+03', true);
INSERT INTO hotel_schema.schedule (schedule_id, task_id, staff_id, room_id, date, date_end, ordered) OVERRIDING SYSTEM VALUE VALUES (6, 1, 5, 103, '2023-09-25 12:00:00+03', '2023-09-25 12:56:00+03', false);
INSERT INTO hotel_schema.schedule (schedule_id, task_id, staff_id, room_id, date, date_end, ordered) OVERRIDING SYSTEM VALUE VALUES (7, 1, 2, 302, '2023-10-06 12:00:00+03', '2023-10-06 13:00:00+03', false);
INSERT INTO hotel_schema.schedule (schedule_id, task_id, staff_id, room_id, date, date_end, ordered) OVERRIDING SYSTEM VALUE VALUES (8, 8, 9, 302, '2023-10-06 13:00:00+03', '2023-10-06 14:30:00+03', false);
INSERT INTO hotel_schema.schedule (schedule_id, task_id, staff_id, room_id, date, date_end, ordered) OVERRIDING SYSTEM VALUE VALUES (9, 1, 8, 202, '2023-10-07 16:00:00+03', '2023-10-07 17:00:00+03', true);
INSERT INTO hotel_schema.schedule (schedule_id, task_id, staff_id, room_id, date, date_end, ordered) OVERRIDING SYSTEM VALUE VALUES (10, 7, 10, 202, '2023-10-08 20:00:00+03', '2023-10-08 21:00:00+03', true);
INSERT INTO hotel_schema.schedule (schedule_id, task_id, staff_id, room_id, date, date_end, ordered) OVERRIDING SYSTEM VALUE VALUES (11, 1, 10, 202, '2023-10-09 12:00:00+03', '2023-10-09 13:07:00+03', false);
INSERT INTO hotel_schema.schedule (schedule_id, task_id, staff_id, room_id, date, date_end, ordered) OVERRIDING SYSTEM VALUE VALUES (12, 1, 4, 102, '2023-10-10 12:00:00+03', '2023-10-10 13:00:00+03', false);
INSERT INTO hotel_schema.schedule (schedule_id, task_id, staff_id, room_id, date, date_end, ordered) OVERRIDING SYSTEM VALUE VALUES (13, 6, 6, 401, '2023-10-19 00:00:00+03', '2023-10-19 00:30:00+03', true);
INSERT INTO hotel_schema.schedule (schedule_id, task_id, staff_id, room_id, date, date_end, ordered) OVERRIDING SYSTEM VALUE VALUES (14, 1, 3, 401, '2023-10-20 12:00:00+03', '2023-10-20 13:00:00+03', false);
INSERT INTO hotel_schema.schedule (schedule_id, task_id, staff_id, room_id, date, date_end, ordered) OVERRIDING SYSTEM VALUE VALUES (15, 2, 7, 303, '2023-10-21 14:00:00+03', '2023-10-21 14:15:00+03', true);
INSERT INTO hotel_schema.schedule (schedule_id, task_id, staff_id, room_id, date, date_end, ordered) OVERRIDING SYSTEM VALUE VALUES (16, 3, 8, 303, '2023-10-22 10:00:00+03', '2023-10-22 10:11:00+03', true);
INSERT INTO hotel_schema.schedule (schedule_id, task_id, staff_id, room_id, date, date_end, ordered) OVERRIDING SYSTEM VALUE VALUES (17, 1, 8, 303, '2023-10-22 12:00:00+03', '2023-10-22 13:00:00+03', false);
INSERT INTO hotel_schema.schedule (schedule_id, task_id, staff_id, room_id, date, date_end, ordered) OVERRIDING SYSTEM VALUE VALUES (18, 8, 3, 303, '2023-10-22 13:00:00+03', '2023-10-22 14:30:00+03', false);
INSERT INTO hotel_schema.schedule (schedule_id, task_id, staff_id, room_id, date, date_end, ordered) OVERRIDING SYSTEM VALUE VALUES (19, 5, 4, 401, '2023-10-27 14:00:00+03', '2023-10-27 14:20:00+03', true);
INSERT INTO hotel_schema.schedule (schedule_id, task_id, staff_id, room_id, date, date_end, ordered) OVERRIDING SYSTEM VALUE VALUES (20, 1, 5, 401, '2023-10-28 12:00:00+03', '2023-10-28 13:00:00+03', false);


--
-- TOC entry 4878 (class 0 OID 16500)
-- Dependencies: 221
-- Data for Name: staff; Type: TABLE DATA; Schema: hotel_schema; Owner: postgres
--

INSERT INTO hotel_schema.staff (staff_id, name, surname, patronymic, passport, experience, salary) OVERRIDING SYSTEM VALUE VALUES (1, 'Мирослава', 'Кузьмина', 'Тимофеевна', 2489563531, 5, 150000);
INSERT INTO hotel_schema.staff (staff_id, name, surname, patronymic, passport, experience, salary) OVERRIDING SYSTEM VALUE VALUES (2, 'Илья', 'Рябчиков', 'Глебович', 7723439783, 5, 120000);
INSERT INTO hotel_schema.staff (staff_id, name, surname, patronymic, passport, experience, salary) OVERRIDING SYSTEM VALUE VALUES (3, 'Мадина', 'Котова', 'Данииловна', 7473016236, 4, 120000);
INSERT INTO hotel_schema.staff (staff_id, name, surname, patronymic, passport, experience, salary) OVERRIDING SYSTEM VALUE VALUES (4, 'Макар', 'Тяпкин', 'Тихонович', 8352698903, 3, 80000);
INSERT INTO hotel_schema.staff (staff_id, name, surname, patronymic, passport, experience, salary) OVERRIDING SYSTEM VALUE VALUES (5, 'Матвей', 'Панкратов', 'Данилович', 4726956084, 3, 80000);
INSERT INTO hotel_schema.staff (staff_id, name, surname, patronymic, passport, experience, salary) OVERRIDING SYSTEM VALUE VALUES (6, 'Дарья', 'Прокофьева', 'Никитична', 9298720193, 3, 90000);
INSERT INTO hotel_schema.staff (staff_id, name, surname, patronymic, passport, experience, salary) OVERRIDING SYSTEM VALUE VALUES (7, 'Андрей', 'Диблев', 'Михайлович', 3111598611, 3, 70000);
INSERT INTO hotel_schema.staff (staff_id, name, surname, patronymic, passport, experience, salary) OVERRIDING SYSTEM VALUE VALUES (8, 'Степан', 'Заборкин', 'Михайлович', 8996907688, 1, 70000);
INSERT INTO hotel_schema.staff (staff_id, name, surname, patronymic, passport, experience, salary) OVERRIDING SYSTEM VALUE VALUES (9, 'Ангелина', 'Дельтапланова', 'Александровна', 1639096166, 0, 50000);
INSERT INTO hotel_schema.staff (staff_id, name, surname, patronymic, passport, experience, salary) OVERRIDING SYSTEM VALUE VALUES (10, 'Полина', 'Читосова', 'Яновна', 2544854603, 0, 50000);


--
-- TOC entry 4880 (class 0 OID 16508)
-- Dependencies: 223
-- Data for Name: task; Type: TABLE DATA; Schema: hotel_schema; Owner: postgres
--

INSERT INTO hotel_schema.task (task_id, name, duration, payment) OVERRIDING SYSTEM VALUE VALUES (1, 'Уборка', 60, 1000);
INSERT INTO hotel_schema.task (task_id, name, duration, payment) OVERRIDING SYSTEM VALUE VALUES (2, 'Пополнение мини-бара', 15, 500);
INSERT INTO hotel_schema.task (task_id, name, duration, payment) OVERRIDING SYSTEM VALUE VALUES (3, 'Завтрак в номер', 15, 300);
INSERT INTO hotel_schema.task (task_id, name, duration, payment) OVERRIDING SYSTEM VALUE VALUES (4, 'Аренда PlayStation 5', 60, 300);
INSERT INTO hotel_schema.task (task_id, name, duration, payment) OVERRIDING SYSTEM VALUE VALUES (5, 'Замена постельного белья и полотенец', 20, 200);
INSERT INTO hotel_schema.task (task_id, name, duration, payment) OVERRIDING SYSTEM VALUE VALUES (6, 'Романтический ужин в номер', 30, 1500);
INSERT INTO hotel_schema.task (task_id, name, duration, payment) OVERRIDING SYSTEM VALUE VALUES (7, 'Няня для ребенка', 60, 800);
INSERT INTO hotel_schema.task (task_id, name, duration, payment) OVERRIDING SYSTEM VALUE VALUES (8, 'Ремонт техники', 90, 1200);
INSERT INTO hotel_schema.task (task_id, name, duration, payment) OVERRIDING SYSTEM VALUE VALUES (9, 'Ароматизированные свечи', 10, 200);


--
-- TOC entry 4875 (class 0 OID 16480)
-- Dependencies: 218
-- Data for Name: visitor; Type: TABLE DATA; Schema: hotel_schema; Owner: postgres
--

INSERT INTO hotel_schema.visitor (visitor_id, name, surname, patronymic, passport, phone_number, gender) OVERRIDING SYSTEM VALUE VALUES (1, 'Арсений', 'Чеботарев', 'Константинович', 2516751141, '+79800649930', 'мужской');
INSERT INTO hotel_schema.visitor (visitor_id, name, surname, patronymic, passport, phone_number, gender) OVERRIDING SYSTEM VALUE VALUES (2, 'Виктория', 'Соколова', 'Александровна', 2619995594, '+79125425286', 'женский');
INSERT INTO hotel_schema.visitor (visitor_id, name, surname, patronymic, passport, phone_number, gender) OVERRIDING SYSTEM VALUE VALUES (3, 'Лев', 'Борисов', 'Тихонович', 3249260990, '+79809970052', 'мужской');
INSERT INTO hotel_schema.visitor (visitor_id, name, surname, patronymic, passport, phone_number, gender) OVERRIDING SYSTEM VALUE VALUES (4, 'Максим', 'Панфилов', 'Ярославович', 3872582487, '+79716269383', 'мужской');
INSERT INTO hotel_schema.visitor (visitor_id, name, surname, patronymic, passport, phone_number, gender) OVERRIDING SYSTEM VALUE VALUES (5, 'Анастасия', 'Николаева', 'Кирилловна', 4124582772, '+79611527987', 'женский');
INSERT INTO hotel_schema.visitor (visitor_id, name, surname, patronymic, passport, phone_number, gender) OVERRIDING SYSTEM VALUE VALUES (6, 'Марта', 'Боброва', 'Андреевна', 4567759433, '+79866776098', 'женский');
INSERT INTO hotel_schema.visitor (visitor_id, name, surname, patronymic, passport, phone_number, gender) OVERRIDING SYSTEM VALUE VALUES (7, 'Степан', 'Лебедев', 'Максимович', 7293639023, '+79203236667', 'мужской');
INSERT INTO hotel_schema.visitor (visitor_id, name, surname, patronymic, passport, phone_number, gender) OVERRIDING SYSTEM VALUE VALUES (8, 'Алёна', 'Кулагина', 'Алексеевна', 7494294166, '+79709925493', 'женский');
INSERT INTO hotel_schema.visitor (visitor_id, name, surname, patronymic, passport, phone_number, gender) OVERRIDING SYSTEM VALUE VALUES (9, 'Михаил', 'Петров', 'Богданович', 8465684418, '+79618326391', 'мужской');
INSERT INTO hotel_schema.visitor (visitor_id, name, surname, patronymic, passport, phone_number, gender) OVERRIDING SYSTEM VALUE VALUES (10, 'Ева', 'Васильева', 'Ивановна', 9134919961, '+79554347862', 'женский');


--
-- TOC entry 4888 (class 0 OID 0)
-- Dependencies: 217
-- Name: booking_booking_id_seq; Type: SEQUENCE SET; Schema: hotel_schema; Owner: postgres
--

SELECT pg_catalog.setval('hotel_schema.booking_booking_id_seq', 10, true);


--
-- TOC entry 4889 (class 0 OID 0)
-- Dependencies: 224
-- Name: schedule_schedule_id_seq; Type: SEQUENCE SET; Schema: hotel_schema; Owner: postgres
--

SELECT pg_catalog.setval('hotel_schema.schedule_schedule_id_seq', 20, true);


--
-- TOC entry 4890 (class 0 OID 0)
-- Dependencies: 220
-- Name: staff_staff_id_seq; Type: SEQUENCE SET; Schema: hotel_schema; Owner: postgres
--

SELECT pg_catalog.setval('hotel_schema.staff_staff_id_seq', 10, true);


--
-- TOC entry 4891 (class 0 OID 0)
-- Dependencies: 222
-- Name: task_task_id_seq; Type: SEQUENCE SET; Schema: hotel_schema; Owner: postgres
--

SELECT pg_catalog.setval('hotel_schema.task_task_id_seq', 9, true);


--
-- TOC entry 4892 (class 0 OID 0)
-- Dependencies: 219
-- Name: visitor_visitor_id_seq; Type: SEQUENCE SET; Schema: hotel_schema; Owner: postgres
--

SELECT pg_catalog.setval('hotel_schema.visitor_visitor_id_seq', 10, true);


--
-- TOC entry 4715 (class 2606 OID 16468)
-- Name: booking booking_pkey; Type: CONSTRAINT; Schema: hotel_schema; Owner: postgres
--

ALTER TABLE ONLY hotel_schema.booking
    ADD CONSTRAINT booking_pkey PRIMARY KEY (booking_id);


--
-- TOC entry 4713 (class 2606 OID 16461)
-- Name: room room_pkey; Type: CONSTRAINT; Schema: hotel_schema; Owner: postgres
--

ALTER TABLE ONLY hotel_schema.room
    ADD CONSTRAINT room_pkey PRIMARY KEY (room_id);


--
-- TOC entry 4723 (class 2606 OID 16522)
-- Name: schedule schedule_pkey; Type: CONSTRAINT; Schema: hotel_schema; Owner: postgres
--

ALTER TABLE ONLY hotel_schema.schedule
    ADD CONSTRAINT schedule_pkey PRIMARY KEY (schedule_id);


--
-- TOC entry 4719 (class 2606 OID 16506)
-- Name: staff staff_pkey; Type: CONSTRAINT; Schema: hotel_schema; Owner: postgres
--

ALTER TABLE ONLY hotel_schema.staff
    ADD CONSTRAINT staff_pkey PRIMARY KEY (staff_id);


--
-- TOC entry 4721 (class 2606 OID 16514)
-- Name: task task_pkey; Type: CONSTRAINT; Schema: hotel_schema; Owner: postgres
--

ALTER TABLE ONLY hotel_schema.task
    ADD CONSTRAINT task_pkey PRIMARY KEY (task_id);


--
-- TOC entry 4717 (class 2606 OID 16486)
-- Name: visitor visitor_pkey; Type: CONSTRAINT; Schema: hotel_schema; Owner: postgres
--

ALTER TABLE ONLY hotel_schema.visitor
    ADD CONSTRAINT visitor_pkey PRIMARY KEY (visitor_id);


--
-- TOC entry 4724 (class 2606 OID 16475)
-- Name: booking room_fkey; Type: FK CONSTRAINT; Schema: hotel_schema; Owner: postgres
--

ALTER TABLE ONLY hotel_schema.booking
    ADD CONSTRAINT room_fkey FOREIGN KEY (room_id) REFERENCES hotel_schema.room(room_id) NOT VALID;


--
-- TOC entry 4726 (class 2606 OID 16533)
-- Name: schedule room_fkey; Type: FK CONSTRAINT; Schema: hotel_schema; Owner: postgres
--

ALTER TABLE ONLY hotel_schema.schedule
    ADD CONSTRAINT room_fkey FOREIGN KEY (room_id) REFERENCES hotel_schema.room(room_id) NOT VALID;


--
-- TOC entry 4727 (class 2606 OID 16528)
-- Name: schedule staff_fkey; Type: FK CONSTRAINT; Schema: hotel_schema; Owner: postgres
--

ALTER TABLE ONLY hotel_schema.schedule
    ADD CONSTRAINT staff_fkey FOREIGN KEY (staff_id) REFERENCES hotel_schema.staff(staff_id) ON DELETE CASCADE NOT VALID;


--
-- TOC entry 4728 (class 2606 OID 16523)
-- Name: schedule task_fkey; Type: FK CONSTRAINT; Schema: hotel_schema; Owner: postgres
--

ALTER TABLE ONLY hotel_schema.schedule
    ADD CONSTRAINT task_fkey FOREIGN KEY (task_id) REFERENCES hotel_schema.task(task_id) NOT VALID;


--
-- TOC entry 4725 (class 2606 OID 16617)
-- Name: booking visitor_fkey; Type: FK CONSTRAINT; Schema: hotel_schema; Owner: postgres
--

ALTER TABLE ONLY hotel_schema.booking
    ADD CONSTRAINT visitor_fkey FOREIGN KEY (visitor_id) REFERENCES hotel_schema.visitor(visitor_id) ON DELETE CASCADE NOT VALID;


-- Completed on 2023-11-16 03:05:25

--
-- PostgreSQL database dump complete
--

