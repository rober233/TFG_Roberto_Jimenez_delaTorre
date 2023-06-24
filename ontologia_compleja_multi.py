
from owlready2 import *
import csv
#owlready2.JAVA_EXE ="C:/Users/rober/OneDrive/Documentos/UPM/TFG/Protege-5.6.1-win/Protege-5.6.1/jre/bin/javaw.exe"


def rules(ont):
	 
	with ont:
		r = list(default_world.sparql("""
			PREFIX tfg:<http://www.semanticweb.org/rober/ontolgia_tfg_2#>
			SELECT ?activo ?inicial ?i ?f
			WHERE{
				{SELECT DISTINCT ?activo ?inicial ?ataque ?imp
				WHERE{
					?activo a tfg:Activo.
					?activo tfg:nivel_de_riesgo ?inicial.
					?ataque a tfg:Ataque.
					?ataque tfg:impacto ?imp.
					?ataque tfg:afecta_al_activo ?activo.
			}}BIND(SUM(?imp) as ?i) BIND((?inicial + ?i) as ?f)}GROUP BY ?activo
				"""))
		print(r)
		for x in range(len(r)):
			for asset in ont.search(type=ont.Activo):
				if asset == r[x][0]:
					asset.nivel_de_riesgo = [int(r[x][3])]

		default_world.sparql("""
			PREFIX tfg:<http://www.semanticweb.org/rober/ontolgia_tfg_2#>
		   		DELETE{
				 ?riesgo tfg:nivel_de_riesgo ?inicial.
			}
			INSERT{
				?riesgo tfg:nivel_de_riesgo ?final.
			}

			WHERE{
				?activo a tfg:Activo.
				?ataque a tfg:Ataque.
				?ataque tfg:afecta_al_activo ?activo.
				?riesgo a tfg:Riesgo.
				?ataque tfg:genera_riesgo ?riesgo.
				?riesgo tfg:nivel_de_riesgo ?inicial.
				?activo tfg:nivel_de_riesgo ?nivel.

			BIND(AVG(?nivel) as ?f)	
			BIND((xsd:integer(?f)) as ?final)
			}

			""")
		ont.save("ontologia_compleja_tfg.owl")


def do_something(batch):
	onto1 = get_ontology("ontologia_V1.owl").load(reload=True)

	
	with onto1:
		for row2 in batch:
			INDEX,ataque,tipo,Ransomware,Trojan,Spyware,subtipo,dlllist_avg_dlls_per_proc,handles_nfile,handles_nkey,handles_nthread,handles_nsemaphore,handles_ntimer,handles_nmutant,ldrmodules_not_in_load,ldrmodules_not_in_mem,ldrmodules_not_in_load_avg,ldrmodules_not_in_init_avg,ldrmodules_not_in_mem_avg,malfind_ninjections,malfind_commitCharge,malfind_protection,svcscan_nservices,svcscan_process_services,svcscan_nactive,callbacks_ncallbacks,impacto ,afecta_al_activo,genera_riesgo= row2
					
			individual_ataque = onto.Ataque("Ataque" + str(INDEX))
			
			if ataque:
				tipo_ataque = str(ataque)
				tipo_onto_ataque = getattr(onto, tipo_ataque)
				individual_ataque.is_a.append(tipo_onto_ataque)
			if tipo:  
				individual_ataque.tipo.append(str(tipo))
			if subtipo:
				individual_ataque.subtipo.append(str(subtipo))
			if Ransomware:
				tipo_Ransomware = str(Ransomware)
				tipo_onto_Ransomware = getattr(onto, tipo_Ransomware)
				individual_ataque.is_a.append(tipo_onto_Ransomware)
			if Trojan:
				tipo_Trojan = str(Trojan)
				tipo_onto_Trojan = getattr(onto, tipo_Trojan)
				individual_ataque.is_a.append(tipo_onto_Trojan)
			if Spyware:
				tipo_Spyware = str(Spyware)
				tipo_onto_Spyware = getattr(onto, tipo_Spyware)
				individual_ataque.is_a.append(tipo_onto_Spyware)
			if impacto:  
				individual_ataque.impacto.append(int(impacto))
			if dlllist_avg_dlls_per_proc:  
				individual_ataque.dlllist_avg_dlls_per_proc = str(dlllist_avg_dlls_per_proc)
			if handles_nfile:  
				individual_ataque.handles_nfile = str(handles_nfile)
			if handles_nkey:  
				individual_ataque.handles_nkey = str(handles_nkey)
			if handles_nthread:  
				individual_ataque.handles_nthread = str(handles_nthread) 
			if handles_nsemaphore:  
				individual_ataque.handles_nsemaphore = str(handles_nsemaphore)
			if handles_ntimer:  
				individual_ataque.handles_ntimer = str(handles_ntimer)
			if handles_nmutant:  
				individual_ataque.handles_nmutant = str(handles_nmutant)
			if ldrmodules_not_in_load:  
				individual_ataque.ldrmodules_not_in_load = str(ldrmodules_not_in_load)
			if ldrmodules_not_in_mem:  
				individual_ataque.ldrmodules_not_in_mem = str(ldrmodules_not_in_mem)
			if ldrmodules_not_in_load_avg:  
				individual_ataque.ldrmodules_not_in_load_avg = str(ldrmodules_not_in_load_avg)
			if ldrmodules_not_in_init_avg:  
				individual_ataque.ldrmodules_not_in_init_avg = str(ldrmodules_not_in_init_avg)
			if ldrmodules_not_in_mem_avg:  
				individual_ataque.ldrmodules_not_in_mem_avg = str(ldrmodules_not_in_mem_avg)
			if malfind_ninjections:  
				individual_ataque.malfind_ninjections = str(malfind_ninjections)
			if malfind_commitCharge:  
				individual_ataque.malfind_commitCharge = str(malfind_commitCharge)
			if malfind_protection:  
				individual_ataque.malfind_protection = str(malfind_protection)
			if svcscan_nservices:  
				individual_ataque.svcscan_nservices = str(svcscan_nservices)
			if svcscan_process_services:  
				individual_ataque.svcscan_process_services = str(svcscan_process_services)
			if svcscan_nactive:  
				individual_ataque.svcscan_nactive = str(svcscan_nactive)
			if callbacks_ncallbacks:  
				individual_ataque.callbacks_ncallbacks = str(callbacks_ncallbacks) 
			if afecta_al_activo:
				afecta_ind = onto.Activo(str(afecta_al_activo))
				individual_ataque.afecta_al_activo.append(afecta_ind)
			if genera_riesgo:
				afecta_indv = onto.Riesgo(str(genera_riesgo))
				individual_ataque.genera_riesgo.append(afecta_indv)
		
		onto1.save("ontologia_V2.owl")
		#onto2.save("ontologia_V3.owl")

		sync_reasoner([onto1])


	onto2 = get_ontology("ontologia_V2.owl").load()
	with onto2:

		onto2.save("ontologia_V3.owl")

		
			
		


	
onto = get_ontology("ontologia_tfg_2.owl").load()
start_time = time.time() 

	# cargar activos

df_activos = open("activos.csv")
reader_df_activos = csv.reader(df_activos)
next(reader_df_activos)

with onto:
			for row1 in reader_df_activos:
				ID,activo,tipo,nivel_de_riesgo,Sistema_operativo= row1
				
				individual_activo = onto.Activo("Activo" + str(ID))

				if activo:
					tipo_activo = str(activo)
					tipo_onto_activo = getattr(onto, tipo_activo)
					individual_activo.is_a.append(tipo_onto_activo)
				if tipo:  
					individual_activo.tipo.append(str(tipo))
				if Sistema_operativo:  
					individual_activo.Sistema_operativo.append(str(Sistema_operativo))    
				if nivel_de_riesgo:
					individual_activo.nivel_de_riesgo.append(int(nivel_de_riesgo))
				
				
				onto.save("ontologia_V1.owl")

	# Cargar ataques

with open('Datos_TFG_Compleja.csv', 'r') as csvfile:
		reader = csv.reader(csvfile)
		header = next(reader) # skip header

		batch_size = 15000
		batch = []
		count = 0

		for row in reader:
			if count >= batch_size:
				do_something(batch)
				batch = []
				count = 0

			batch.append(row)
			count += 1
		if batch:
			do_something(batch)	


onto3=get_ontology("ontologia_V3.owl").load()
rules(onto3)

end_time = time.time()

total_time = end_time-start_time

print(total_time,batch_size)