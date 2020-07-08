
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

        const departamento_resumen_d =results.fecha1_resumen;
        const fecha2_resumen_d =results.fecha2_resumen;
       
        const [labels,data]=[
            Object.keys(departamento_resumen_d),
            Object.values(departamento_resumen_d),
        ];
        const [labels2,data2]=[
            Object.keys(fecha2_resumen_d),
            Object.values(fecha2_resumen_d),
        ];
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
        type: 'pie',
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
//segundoooo
const renderChart_dept1 =(data,labels)=>{
    
    var ctx = document.getElementById('myChart_dep1').getContext('2d');
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


const getChartData_dep1 =()=>{
   
    fetch('/dep1_resumen')
    .then((res)=>res.json())
    .then((results)=>{
        console.log ("results",results);

        const dep1_resumen_d =results.dep1_resumen;
        const [labels,data]=[
            Object.keys(dep1_resumen_d),
            Object.values(dep1_resumen_d),
        ];
        renderChart_dept1(data,labels);
    });
};



document.onload = getChartData();
document.onload = getChartData_dep1();
document.onload = getChartDataGenero();
document.onload = getChartDatafechas();