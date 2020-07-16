function porMunicipio_fechas(id) {

    
    const renderChartFechas_muni =(data,labels,data2)=>{

        var ctx = document.getElementById('dashboardMuni').getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Cantidad de pruebas Positivas',
                    data: data,
                    backgroundColor: [
                        'rgba(33, 36, 89, 0.7)',
                        'rgba(2, 100, 140, 0.7)',
                        'rgba(2, 140, 140, 0.7)',
                        'rgba(4, 191, 172, 0.7)',
                        'rgba(153, 102, 255, 0.7)',
                        'rgba(255, 159, 64, 0.7)'
                    ],
                    borderColor: [
                        'rgba(33, 36, 89, 1)',
                        'rgba(2, 100, 140, 1)',
                        'rgba(2, 140, 140, 1)',
                        'rgba(4, 191, 172, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)'
                    ],
                    borderWidth: 1
                },{
                    label: 'Cantidad de pruebas Realizadas',
                    data: data2,
                    backgroundColor: [
                        'rgba(2, 100, 140, 0.7)',
                        'rgba(33, 36, 89, 0.7)',                 
                        'rgba(2, 140, 140, 0.7)',
                        'rgba(4, 191, 172, 0.7)',
                        'rgba(153, 102, 255, 0.7)',
                        'rgba(255, 159, 64, 0.7)'
                    ],
                    borderColor: [
                        'rgba(2, 100, 140, 1)',
                        'rgba(33, 36, 89, 1)',
                        'rgba(2, 140, 140, 1)',
                        'rgba(4, 191, 172, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                legend: {
                    display: true
                },
               
            }
        });
    }
    
    
    const getChartData_fun =()=>{
       
     
        fetch('/fechas_resumen_muni/'+id)
        .then((res)=>res.json())
        .then((results)=>{
            console.log ("results",results);
    
            const posi_resumen =results.positivas_resumen;
            const prue_resumen =results.pruebas_resumen;
           
            const [labels,data]=[
                Object.keys(posi_resumen),
                Object.values(posi_resumen),
            ];
            const [labels2,data2]=[
                Object.keys(prue_resumen),
                Object.values(prue_resumen),
            ];
            ad1 = data;
            renderChartFechas_muni(data,labels,data2);
        });
       
    };
getChartData_fun();
}


function porMunicipio_edades(id) {

    
    const renderChartEdades =(data,labels)=>{
    
        var ctx = document.getElementById('dashboardEdades').getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'polarArea',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Cantidad de pruebas',
                    data: data,
                    backgroundColor: [
                        'rgba(33, 36, 89, 0.7)',
                        'rgba(2, 100, 140, 0.7)',
                        'rgba(2, 140, 140, 0.7)',
                        'rgba(4, 191, 172, 0.7)',
                        'rgba(153, 102, 255, 0.7)',
                        'rgba(255, 159, 64, 0.7)'
                    ],
                    borderColor: [
                        'rgba(33, 36, 89, 1)',
                        'rgba(2, 100, 140, 1)',
                        'rgba(2, 140, 140, 1)',
                        'rgba(4, 191, 172, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)'
                    ],
    
    
    
                    borderWidth: 1
                }]
            },
            options: {
               
                legend: {
                    display: true,
                    position: 'left',
                    labels: {
                        boxWidth: 20
                    }
                },
               
            }
        });
    }
    
    
    const getChartDataEdades =()=>{
       
        fetch('/edades_resumen_muni/'+id)
        .then((res)=>res.json())
        .then((results)=>{
            console.log ("results",results);
    
            const departamento_resumen_d =results.edad_resumen;
            const [labels,data]=[
                Object.keys(departamento_resumen_d),
                Object.values(departamento_resumen_d),
            ];
            renderChartEdades(data,labels);
        });
    };
    getChartDataEdades();
}



function getid_muni()
{
    var id = document.getElementById('idMuni').value;
    porMunicipio_fechas(id);
    porMunicipio_edades(id);
}
document.onload = getid_muni();