#!/bin/bash

start_date=$1

# Grab all the data
psql -h dbsrv adbs <<EOF >app_data.json
select json_agg(e) from
(select program, description, type, status, keeper,
backup, author, mod_on, mod_by, sqa_level, cpld.execution_count,
map.index_page
from schumann.mecca_view_program_info pg
left join (select prog, count(*) as execution_count
		   from smeding.v_cpld_pgm_log where start >
		   '$start_date'::timestamp with time zone at time zone
		   '-06' group by prog) cpld on pg.program = cpld.prog
left join (select concat('pa', lpad(pa_number::text, 4, '0'))
		   pa_number, array_agg(concat(id,page_number)) as
		   index_page from schumann.index_page_view_entries
		   where pa_number is not null group by pa_number) map
		   on map.pa_number = pg.program
where pg.type = 'pas' or pg.type = 'sas') e;
EOF
