/*
 Navicat Premium Data Transfer

 Source Server         : ETC-DEV
 Source Server Type    : PostgreSQL
 Source Server Version : 110005
 Source Host           : 192.168.56.105:5432
 Source Catalog        : postgres
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 110005
 File Encoding         : 65001

 Date: 06/05/2022 13:18:19
*/


-- ----------------------------
-- Table structure for cruces
-- ----------------------------
DROP TABLE IF EXISTS "public"."cruces";
CREATE TABLE "public"."cruces" (
  "id" int4 NOT NULL,
  "carril" varchar(255) COLLATE "pg_catalog"."default",
  "fecha" varchar(255) COLLATE "pg_catalog"."default",
  "hora_plaza" varchar(255) COLLATE "pg_catalog"."default",
  "antena" varchar(255) COLLATE "pg_catalog"."default",
  "tag" varchar(255) COLLATE "pg_catalog"."default",
  "estatus" varchar(255) COLLATE "pg_catalog"."default",
  "cruce" varchar(255) COLLATE "pg_catalog"."default",
  "eje" varchar(255) COLLATE "pg_catalog"."default",
  "rodada" varchar(255) COLLATE "pg_catalog"."default",
  "clase" varchar(255) COLLATE "pg_catalog"."default",
  "evento_carril" varchar(255) COLLATE "pg_catalog"."default",
  "t_vehiculo" varchar(255) COLLATE "pg_catalog"."default",
  "turno" int4,
  "sentido" varchar(255) COLLATE "pg_catalog"."default",
  "fecha_hora_utc" varchar(255) COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Records of cruces
-- ----------------------------
INSERT INTO "public"."cruces" VALUES (1, '2308', '20220202', '130634', '0000089494', 'OPER1-22939979', '01', '00', '05', '001', '05', '0000092546', '02', 2, 'B', '20160221200634');
INSERT INTO "public"."cruces" VALUES (1, '2308', '20220202', '130634', '0000089494', 'OPER1-22939979', '01', '00', '05', '001', '05', '0000092546', '02', 2, 'B', '20160221200634');
