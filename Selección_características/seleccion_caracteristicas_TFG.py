# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 20:19:31 2023

@author: Roberto Jiménez de la Torre
"""

#importamos las librerias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from matplotlib import pyplot
#%%

#IMPORTAMOS LA BASE DE DATOS
#damos el nombre a las variables
variables = ['pslist.nproc','pslist.nppid','pslist.avg_threads','pslist.nprocs64bit','pslist.avg_handlers','dlllist.ndlls','dlllist.avg_dlls_per_proc','handles.nhandles','handles.avg_handles_per_proc','handles.nport','handles.nfile','handles.nevent','handles.ndesktop','handles.nkey','handles.nthread','handles.ndirectory','handles.nsemaphore','handles.ntimer','handles.nsection','handles.nmutant','ldrmodules.not_in_load','ldrmodules.not_in_init','ldrmodules.not_in_mem','ldrmodules.not_in_load_avg','ldrmodules.not_in_init_avg','ldrmodules.not_in_mem_avg','malfind.ninjections','malfind.commitCharge','malfind.protection','malfind.uniqueInjections','psxview.not_in_pslist','psxview.not_in_eprocess_pool','psxview.not_in_ethread_pool','psxview.not_in_pspcid_list','psxview.not_in_csrss_handles','psxview.not_in_session','psxview.not_in_deskthrd','psxview.not_in_pslist_false_avg','psxview.not_in_eprocess_pool_false_avg','psxview.not_in_ethread_pool_false_avg','psxview.not_in_pspcid_list_false_avg','psxview.not_in_csrss_handles_false_avg','psxview.not_in_session_false_avg','psxview.not_in_deskthrd_false_avg','modules.nmodules','svcscan.nservices','svcscan.kernel_drivers','svcscan.fs_drivers','svcscan.process_services','svcscan.shared_process_services','svcscan.interactive_process_services','svcscan.nactive','callbacks.ncallbacks','callbacks.nanonymous','callbacks.ngeneric','Class','Category']
variables_imp = ['pslist.nproc','pslist.nppid','pslist.avg_threads','pslist.nprocs64bit','pslist.avg_handlers','dlllist.ndlls','dlllist.avg_dlls_per_proc','handles.nhandles','handles.avg_handles_per_proc','handles.nport','handles.nfile','handles.nevent','handles.ndesktop','handles.nkey','handles.nthread','handles.ndirectory','handles.nsemaphore','handles.ntimer','handles.nsection','handles.nmutant','ldrmodules.not_in_load','ldrmodules.not_in_init','ldrmodules.not_in_mem','ldrmodules.not_in_load_avg','ldrmodules.not_in_init_avg','ldrmodules.not_in_mem_avg','malfind.ninjections','malfind.commitCharge','malfind.protection','malfind.uniqueInjections','psxview.not_in_pslist','psxview.not_in_eprocess_pool','psxview.not_in_ethread_pool','psxview.not_in_pspcid_list','psxview.not_in_csrss_handles','psxview.not_in_session','psxview.not_in_deskthrd','psxview.not_in_pslist_false_avg','psxview.not_in_eprocess_pool_false_avg','psxview.not_in_ethread_pool_false_avg','psxview.not_in_pspcid_list_false_avg','psxview.not_in_csrss_handles_false_avg','psxview.not_in_session_false_avg','psxview.not_in_deskthrd_false_avg','modules.nmodules','svcscan.nservices','svcscan.kernel_drivers','svcscan.fs_drivers','svcscan.process_services','svcscan.shared_process_services','svcscan.interactive_process_services','svcscan.nactive','callbacks.ncallbacks','callbacks.nanonymous','callbacks.ngeneric']

#importamos el archivo csv
data = pd.read_csv('seleccion_caracteristicas.csv', names = variables, delimiter = ";",header = 0)
#print(fram_data)




print(data)


#FUNCIONES UTILIZADAS 

#------------------------Normalización de los datos---------------------------
def normalizar(X_train, X_test):
    Min_Max = MinMaxScaler()
    Min_Max.fit(X_train)
    X_train_norm = Min_Max.transform(X_train)
    X_test_norm = Min_Max.transform(X_test)
    
    #Normalizamos los datos 
       
    return X_train_norm, X_test_norm


#--------------------------------BALANCEADO DE DATOS------------------------- 

# example of random undersampling to balance the class distribution
from collections import Counter
from sklearn.datasets import make_classification





 
# prepare input data
def prepare_inputs(X_train, X_test):
	oe = OrdinalEncoder()
	oe.fit(X_train)
	X_train_enc = oe.transform(X_train)
	X_test_enc = oe.transform(X_test)
	return X_train_enc, X_test_enc
 
# prepare target
def prepare_targets(y_train, y_test):
	le = LabelEncoder()
	le.fit(y_train)
	y_train_enc = le.transform(y_train)
	y_test_enc = le.transform(y_test)
	return y_train_enc, y_test_enc
 


#---------------------------Graficos importancia y diferencias-----------------


def graficos_filter(var_imp):
    
    #Calculamos la media de la importancia para cada variable 
    mean_df = var_imp.mean()
    #creamos un df con las medias
    df_rep = pd.DataFrame(mean_df, columns = ['Importancia'])
    print(df_rep)
    #lo ordenamos de mayor a menos
    df_rep = df_rep.sort_values(by='Importancia', ascending=False)

    #las variables son los indices
    var = df_rep.index.tolist()

    print(df_rep)
    #Representamos la importancia de las variables
    pyplot.bar(var, df_rep['Importancia'])
    plt.title('Importancia de las variables utilizando ' + a, fontsize=16)
    plt.xlabel('\n Variables', fontsize=14)
    plt.ylabel('Importancia \n', fontsize=14)
    plt.xticks(fontsize=10)
    plt.xticks(rotation=70)
    plt.yticks(fontsize=12)
    plt.show()
     
    #Representamos las diferencias 
    dif = []
    nombres_val = []
    for j in range(1,len(df_rep['Importancia'])):
        dif.append((df_rep['Importancia'][j-1])-(df_rep['Importancia'][j]))
        nombres_val.append(var[j-1]+'-'+var[j])
        
    #Grafico de las diferencias 
    pyplot.bar(range(0,len(df_rep)-1), dif)
    plt.title('Diferencias entre importancias utilizando ' + a)
    plt.xlabel('\n Variables', fontsize=14)
    plt.ylabel('Diferencia \n', fontsize=14)
    plt.xticks(range(0,len(df_rep)-1), nombres_val)
    plt.xticks(fontsize=10)
    plt.xticks(rotation=70)
    pyplot.show()   
    
   # print(dif)

    #print(nombres_val)
    


 

#Separamos en X e y 
X = pd.DataFrame(data.drop(labels=['Category', 'Class'],axis=1))
y = pd.DataFrame(data['Category'])
y = y.astype("category")

    


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y.values.ravel())
print(y)


clasificador = 'RF'
a = 'RF'


var_imp = pd.DataFrame(columns = variables_imp) #En CHI cogemos variables_disc_nombre
var_imp_pvalor = pd.DataFrame(columns = variables_imp) #En CHI cogemos variables_disc_nombre

for idx in range(1,6): #Hacemos 5 particiones 
    
    #Dividimos en train y test el conjuntos balanceado
    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.3, random_state=idx)
    

    
    #Normalizamos
    X_train, X_test = normalizar(X_train, X_test)
    
        
         
    #Seleccion de hiperparametros
    n_estimators = [int(x) for x in np.linspace(start = 200, stop = 2000, num = 10)]
    max_features = ['auto', 'sqrt']
    max_depth = [int(x) for x in np.linspace(10, 110, num = 11)]
    max_depth.append(None)
    min_samples_split = [2, 5, 10]
    min_samples_leaf = [1, 2, 4]
    bootstrap = [True, False]
    # Hiperparámetros posibles
    hiper_pos = {'n_estimators': n_estimators,
                   'max_features': max_features,
                   'max_depth': max_depth,
                   'min_samples_split': min_samples_split,
                   'min_samples_leaf': min_samples_leaf,
                   'bootstrap': bootstrap}
   
    rf = RandomForestClassifier()
    rf = RandomizedSearchCV(estimator = rf, param_distributions = hiper_pos, n_iter = 100, cv = 3, verbose=2, random_state=42, n_jobs = -1)
    rf.fit(X_train, Y_train.ravel())
   
    rf_best =  rf.best_estimator_
    print(rf.best_params_)
   
    #Aplico el modelo con los hiperparametros seleccionados 
    model = rf_best
    # fit the model
    model.fit(X_train, Y_train.values.ravel())
    
    # nos quedamos con los coeficientes
    importancia = model.feature_importances_
    fs_rf=importancia
    fs_rf = list(fs_rf)
    var_imp.loc[idx] = fs_rf
           
   
        
graficos_filter(var_imp)
print(a)

# %%
