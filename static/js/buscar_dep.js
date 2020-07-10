
const renderChartFechas =(data,labels,data2)=>{
    
    var ctx = document.getElementById('myChartfechas').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Cantidad de pruebas Positivas',
                data: data,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.7)',
                    'rgba(54, 162, 235, 0.7)',
                    'rgba(255, 206, 86, 0.7)',
                    'rgba(75, 192, 192, 0.7)',
                    'rgba(153, 102, 255, 0.7)',
                    'rgba(255, 159, 64, 0.7)'
                ],
                borderColor: [
                    'rgba(255, 206, 86, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 99, 132, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            },{
                label: 'Cantidad de pruebas Realizadas',
                data: data2,
                backgroundColor: [
                    'rgba(54, 162, 235, 0.7)',
                    'rgba(255, 99, 132, 0.7)',
                    'rgba(255, 206, 86, 0.7)',
                    'rgba(75, 192, 192, 0.7)',
                    'rgba(153, 102, 255, 0.7)',
                    'rgba(255, 159, 64, 0.7)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
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


const getChartDatafechas =()=>{
   
 
    fetch('/fechas_resumen')
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
        renderChartFechas(data,labels,data2);
    });
   
};
//departamentos
const renderChart =(data,labels)=>{
    
    var ctx = document.getElementById('myChart_departamentos').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: labels,
            datasets: [{
                label: 'Cantidad de pruebas',
                data: data,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.7)',
                    'rgba(54, 162, 235, 0.7)',
                    'rgba(255, 206, 86, 0.7)',
                    'rgba(75, 192, 192, 0.7)',
                    'rgba(153, 102, 255, 0.7)',
                    'rgba(255, 159, 64, 0.7)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
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


const getChartData =()=>{
   
    fetch('/departamentos_resumen')
    .then((res)=>res.json())
    .then((results)=>{
        console.log ("results",results);

        const departamento_resumen_d =results.departamento_resumen;
        const [labels,data]=[
            Object.keys(departamento_resumen_d),
            Object.values(departamento_resumen_d),
        ];
        renderChart(data,labels);
    });
};
//generro genero_resumen
const renderChartGenero =(data,labels)=>{
    
    var ctx = document.getElementById('myChart_genero').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: labels,
            datasets: [{
                label: 'Cantidad de pruebas positivas',
                data: data,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.7)',
                    'rgba(54, 162, 235, 0.7)',
                    'rgba(255, 206, 86, 0.7)',
                    'rgba(75, 192, 192, 0.7)',
                    'rgba(153, 102, 255, 0.7)',
                    'rgba(255, 159, 64, 0.7)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
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


const getChartDataGenero =()=>{
   
    fetch('/genero_resumen')
    .then((res)=>res.json())
    .then((results)=>{
        console.log ("results",results);

        const genero_d =results.genero_resumen;
        const [labels,data]=[
            Object.keys(genero_d),
            Object.values(genero_d),
        ];
        renderChartGenero(data,labels);
    });
};

//funcion_

function porDepartamento(id) {

   
    const renderChart_fun=(data,labels)=>{
    
        var ctx = document.getElementById('chart_departamento-'+id).getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: '# of Votes',
                    data: data,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.7)',
                        'rgba(54, 162, 235, 0.7)',
                        'rgba(255, 206, 86, 0.7)',
                        'rgba(75, 192, 192, 0.7)',
                        'rgba(153, 102, 255, 0.7)',
                        'rgba(255, 159, 64, 0.7)'
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                legend: {
                    display: false
                },
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });
        
    }
    
    
    const getChartData_fun =()=>{
       
        fetch('/dep1_resumen/'+id)
        .then((res)=>res.json())
        .then((results)=>{
            console.log ("results",results);
    
            const dep1_resumen_d =results.dep1_resumen;
          
            const [labels,data]=[
                Object.keys(dep1_resumen_d),
                Object.values(dep1_resumen_d),
            ];
            renderChart_fun(data,labels);
        });
    };
    getChartData_fun();
}


function cargarpordep() {
    for (i = 1; i < 15; i++) {
        document.onload = porDepartamento(i);
    }

}
document.onload = getChartData();

document.onload = getChartDataGenero();
document.onload = getChartDatafechas();

document.onload = cargarpordep();