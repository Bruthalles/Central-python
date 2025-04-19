export async function guardarCar(){
           
    let marca = document.getElementById("marca").value.trim();
    let modelo = document.getElementById("modelo").value.trim();
    let ano = document.getElementById("ano").value.trim();

    if (!marca || !modelo || !ano){
        alert("Preencha todos os campos!");
        return;
    }
    const postcar = await fetch("http://127.0.0.1:5000/garage",{method: "POST", headers:{
        "Content-Type":"application/json"
    }, body: JSON.stringify({marca,modelo,ano})
    });

    const dados = await postcar.json();
    const carro = dados.carro;

    if (carro){
    document.getElementById("garage").innerHTML = `
        <section>
            <p><strong>Marca:</strong> ${dados.carro.marca}</p>
        <p><strong>Modelo:</strong> ${dados.carro.modelo}</p>
        <p><strong>Ano:</strong> ${dados.carro.ano}</p>
        
        </section>`;
    }
    else{
        alert("Erro ao carregar o  carro");
    }

};

window.guardarCar = guardarCar;

