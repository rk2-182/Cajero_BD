drop database bancoCripto;
create database bancoCripto;
use bancoCripto;

CREATE TABLE IF NOT EXISTS usuarios_banco(
	id			int(25) auto_increment not null,
    monto_total decimal(19.4),
    rut	varchar(45),
    nombre varchar (45),
    clave varchar(255),
    constraint pk_usuario primary key(id),
    constraint uq_rut unique(rut)
)ENGINE=InnoDB;

insert into usuarios_banco values (null,100000,"181633220","ricardo");
insert into usuarios_banco values (null,100000,"17890990","gabreiela");
insert into usuarios_banco values (null,90000,"181623449","mateo");
/**********************************************************************************/
insert into usuarios_banco (rut)values ("191634562");
insert into usuarios_banco (monto_total,rut,nombre,clave)values (0,"181633220","ricardo rodriguez","9999");

delete from usuarios_banco where id = 1;

update usuarios_banco set monto_total = monto_total + 30000 where rut="181633220";

select * from usuarios_banco where rut = "181633220" and clave = "1234";

select * from usuarios_banco;