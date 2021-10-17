import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-prova2',
  templateUrl: './addItem.component.html',
  styleUrls: ['./addItem.component.css']
})
export class addItemComponent implements OnInit {
  // @ts-ignore
  overlay:object;
  // @ts-ignore
  popup:object;
  // @ts-ignore
  btnAbrirPopup:object;
  // @ts-ignore
  btnCerrarPopup:object;

  constructor() { }

  ngOnInit(): void {
  }
      // @ts-ignore
    overlay = document.getElementById('overlay')
      // @ts-ignore
    popup = document.getElementById('popup')
    // @ts-ignore
    btnAbrirPopup = document.getElementById('btn-abrir-popup')
    // @ts-ignore
    btnCerrarPopup = document.getElementById('btn-cerrar-popup')
     // @ts-ignore
    product_name = document.getElementById('product_name')
    // @ts-ignore
    product_img = document.getElementById('product_img')
    // @ts-ignore
    product_price = document.getElementById('product_price')
   // @ts-ignore
    product_desc = document.getElementById('product_desc')





  open(){
    // @ts-ignore
    overlay.classList.add('active');
    // @ts-ignore
    popup.classList.add('active');
  }
  close(){
    // @ts-ignore
    popup.classList.remove('active');
      // @ts-ignore
    overlay.classList.remove('active');



  }
  onFile(event: any){
    // @ts-ignore
    event.target.files[0].name
  }
  postProduct(){

    // @ts-ignore
    if(product_name.value.length < 3){
      // @ts-ignore
      product_name.style.border = "2px solid red"
    }
    // @ts-ignore
    else if(isNaN(Number(product_price.value)) == true){
      // @ts-ignore
      product_price.style.border = "2px solid red"
    }
    // @ts-ignore
    else if(product_desc.value.length < 5){
      // @ts-ignore
      product_desc.style.border = "2px solid red"
    }
    // @ts-ignore
    else if(event.target.files[0].name.length < 5){
      // @ts-ignore
      product_img.style.border = "2px solid red"
    }
    else{
      // @ts-ignore
      overlay.classList.remove('active');
      // @ts-ignore
      popup.classList.remove('active');
    }


  }


}
