$('form input[type="file"]').change(event => {
  let arquivos = event.target.files;
  if (arquivos.length === 0) {
    console.log('sem imagem pra mostrar')
  } else {
      if(arquivos[0].type == 'image/jpeg') {
        $('img').remove();
        let imagem = $('<img class="img-responsive">');
        imagem.attr('src', window.URL.createObjectURL(arquivos[0]));
        $('figure').prepend(imagem);
      } else {
        alert('Formato não suportado')
      }
  }
});

function Avaliar(estrela) {
    var url = window.location;
    url = url.toString()
    url = url.split("novo.html");
    url = url[1];

    var s1 = document.getElementById("s1").src;
    var s2 = document.getElementById("s2").src;
    var s3 = document.getElementById("s3").src;
    var s4 = document.getElementById("s4").src;
    var s5 = document.getElementById("s5").src;
    var avaliacao = 1;

    //ESTRELA 5
    if (estrela == 5){
        if (s5 == url + "uploads/star0.png") {
             document.getElementById("s1").src = "uploads/star1.png";
             document.getElementById("s2").src = "uploads/star1.png";
             document.getElementById("s3").src = "uploads/star1.png";
             document.getElementById("s4").src = "uploads/star1.png";
             document.getElementById("s5").src = "uploads/star1.png";
             avaliacao = 6;
        } else {
             document.getElementById("s1").src = "uploads/star1.png";
             document.getElementById("s2").src = "uploads/star1.png";
             document.getElementById("s3").src = "uploads/star1.png";
             document.getElementById("s4").src = "uploads/star1.png";
             document.getElementById("s5").src = "uploads/star1.png";
             avaliacao = 5;
        }
    }

    //ESTRELA 4
    if (estrela == 4){
        if (s4 == url + "uploads/star0.png") {
             document.getElementById("s1").src = "uploads/star1.png";
             document.getElementById("s2").src = "uploads/star1.png";
             document.getElementById("s3").src = "uploads/star1.png";
             document.getElementById("s4").src = "uploads/star1.png";
             document.getElementById("s5").src = "uploads/star0.png";
             avaliacao = 5;
        } else {
             document.getElementById("s1").src = "uploads/star1.png";
             document.getElementById("s2").src = "uploads/star1.png";
             document.getElementById("s3").src = "uploads/star1.png";
             document.getElementById("s4").src = "uploads/star1.png";
             document.getElementById("s5").src = "uploads/star0.png";
             avaliacao = 4;
        }
    }

    //ESTRELA 3
    if (estrela == 3){
         if (s3 == url + "uploads/star0.png") {
             document.getElementById("s1").src = "uploads/star1.png";
             document.getElementById("s2").src = "uploads/star1.png";
             document.getElementById("s3").src = "uploads/star1.png";
             document.getElementById("s4").src = "uploads/star0.png";
             document.getElementById("s5").src = "uploads/star0.png";
             avaliacao = 4;
         } else {
             document.getElementById("s1").src = "uploads/star1.png";
             document.getElementById("s2").src = "uploads/star1.png";
             document.getElementById("s3").src = "uploads/star1.png";
             document.getElementById("s4").src = "uploads/star0.png";
             document.getElementById("s5").src = "uploads/star0.png";
             avaliacao = 3;
         }
    }

    //ESTRELA 2
    if (estrela == 2){
         if (s2 == url + "uploads/star0.png") {
             document.getElementById("s1").src = "uploads/star1.png";
             document.getElementById("s2").src = "uploads/star1.png";
             document.getElementById("s3").src = "uploads/star0.png";
             document.getElementById("s4").src = "uploads/star0.png";
             document.getElementById("s5").src = "uploads/star0.png";
             avaliacao = 3;
         } else {
             document.getElementById("s1").src = "uploads/star1.png";
             document.getElementById("s2").src = "uploads/star1.png";
             document.getElementById("s3").src = "uploads/star0.png";
             document.getElementById("s4").src = "uploads/star0.png";
             document.getElementById("s5").src = "uploads/star0.png";
             avaliacao = 2;
         }
    }

    //ESTRELA 1
    if (estrela == 1){
         if (s1 == url + "uploads/star0.png") {
             document.getElementById("s1").src = "uploads/star1.png";
             document.getElementById("s2").src = "uploads/star0.png";
             document.getElementById("s3").src = "uploads/star0.png";
             document.getElementById("s4").src = "uploads/star0.png";
             document.getElementById("s5").src = "uploads/star0.png";
             avaliacao = 2;
         } else {
             document.getElementById("s1").src = "uploads/star1.png";
             document.getElementById("s2").src = "uploads/star0.png";
             document.getElementById("s3").src = "uploads/star0.png";
             document.getElementById("s4").src = "uploads/star0.png";
             document.getElementById("s5").src = "uploads/star0.png";
             avaliacao = 1;
         }
    }

    document.getElementById('rating').innerHTML = avaliacao;

}