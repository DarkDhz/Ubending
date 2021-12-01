import {Component, Inject, OnInit} from '@angular/core';
import {Router} from "@angular/router";
import axios from "axios";
import {environment} from "../../enviroment";
import {MAT_DIALOG_DATA, MatDialog, MatDialogRef} from "@angular/material/dialog";
import {UploadService} from "../../services/upload.service";
import {FormControl, FormGroup, Validators} from "@angular/forms";

export interface DialogData {
  idProduct: Number;
  nameProduct: string;
  priceProduct: string;
  descProduct: string;
  image: string;
}
@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css']
})
export class ProductsComponent implements OnInit {

  isLogged = false;
  token = "null";
  state = {products: []}

  constructor(public dialog: MatDialog,private router: Router) {
    const currentUser = JSON.parse(<string>localStorage.getItem('currentUser'));
    if (currentUser != null) {
      this.token = currentUser.token;
      this.isLogged = true;
    }

  }

  ngOnInit(): void {
    this.getProducts()

    const search = document.getElementById("search"); //pass the id of the input of searchbar
    const products = document.getElementsByClassName("product_name")
    const btns = document.querySelectorAll('.btn');
    const storeProducts = document.getElementsByClassName("product_card")

    search!.addEventListener("keyup", filterProducts);

    function filterProducts(e:any){
      const text = e.target.value.toLowerCase();
      for (let i = 0; i < products.length; i++) {
        // @ts-ignore
        const item = products.item(i).firstChild!.textContent;
        if (item!.toLowerCase().indexOf(text) != -1) {
          // @ts-ignore
          products.item(i).parentElement!.parentElement!.style.display = "block"
        } else {
          // @ts-ignore
          products.item(i).parentElement!.parentElement!.style.display = "none"
        }
      }
    }

    for (let i = 0; i < btns.length; i++) {

      btns[i].addEventListener('click', (e) => {
        for(let x=0; x<btns.length; x++)
        {
          btns[x].classList.remove('active');
        }
        btns[i].classList.add('active');

        e.preventDefault()

        // @ts-ignore
        const filter = e.target.dataset.filter;

        for (let x = 0; x < storeProducts.length; x++) {
          // @ts-ignore
          console.log(storeProducts.item(x).classList)
          if (filter === 'all'){
            // @ts-ignore
            storeProducts.item(x).style.display = 'block'
          } else {
            // @ts-ignore
            if (storeProducts.item(x).classList.contains(filter)){
              // @ts-ignore
              storeProducts.item(x).style.display = 'block'
            } else {
              // @ts-ignore
              storeProducts.item(x).style.display = 'none'
            }
          }

        }

      });
    }
  }

  loadPorducts(name: String) {

  }

  getProducts(){

    const path = environment.path + '/api/search'
    const params = {
      name: '',
      from: 0,
      jump: 20
    }
    axios.post(path, params)
      .then((res) => {
        // @ts-ignore
        this.state.products = res.data
        console.log(res.data)
      })
      .catch((error) => {
        console.error(error)
      })
  }

  onClickSignIn(){
    // @ts-ignore
    this.$router.replace({path: '/', query: {}})
  }

  menuToggle(){
    const toggleMenu = document.querySelector('.menu')
    toggleMenu!.classList.toggle('active')
  }

  resetToken() {
    localStorage.removeItem('currentUser')
    this.router.navigate(['/login-signup'])
  }

  myProducts() {
    this.router.navigate(['/user-products'])
  }

  editProfile() {
    this.router.navigate(['/user-profile'])
  }
  openDialogPayment(idProduct:Number,nameProduct:String,descProduct:String,priceProduct:Number,imagePath:String) {
    const dialogRef = this.dialog.open(Payment, {panelClass: 'custom-modalbox',
      data: {idProduct: idProduct,nameProduct: nameProduct,priceProduct:priceProduct, descProduct:descProduct,image: imagePath}});

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
    });
  }

}

@Component({
  selector: 'payment',
  templateUrl: 'payment.html',
  styleUrls: ['payment.css']
})

export class Payment {
  userEmail = new FormGroup({
    email: new FormControl('', [
      Validators.required,
      Validators.pattern("^[a-zA-Z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,4}$")])
  ,
      name: new FormControl('', [
        Validators.required,
        Validators.pattern("^[a-zA-Z]{2,10} [a-zA-Z ]{2,100}$")]),

      cardNumber: new FormControl('', [
        Validators.required,
        Validators.pattern("^[a-zA-Z0-9]{16,16}$")]),
      date: new FormControl('', [
        Validators.required,
        Validators.pattern("^[0-12]+/+[0-30]{2,2}$")]),
      CVV: new FormControl('', [
        Validators.required,
        Validators.pattern("^[0-9]{3,3}$")]),
      postalCode: new FormControl('', [
        Validators.required,
        Validators.pattern("^[0-9]{5,5}$")]),
      direction: new FormControl('', [
        Validators.required,
        Validators.pattern("^[a-zA-Z0-9]{2,100}$")])
    }

    );

  showAlertInvalidEmail = false;
  showAlertInvalidName = false;
  showAlertInvalidCard = false;
  showAlertInvalidDate = false;
  showAlertInvalidCVV = false;
  showAlertInvalidPostalCode = false;
  showAlertInvalidDirection= false;
  showAlertRequired = false;

  token = "null";
  constructor(
    public dialogRef: MatDialogRef<Payment>,
    @Inject(MAT_DIALOG_DATA) public data: DialogData,private uploadService: UploadService,
    private router: Router) {

      const currentUser = JSON.parse(<string>localStorage.getItem('currentUser'));
      if (currentUser != null) {
        this.token = currentUser.token;
      } else {
        alert('NOT LOGGED IN')
        this.router.navigate(['/home']);
      }


  }
  onNoClick(): void {
    this.dialogRef.close();
  }
  get emailUser(){
      return this.userEmail.get('email')
  }
  get cardUser(){
    return this.userEmail.get('cardNumber')
  }
  get nameUser(){
    return this.userEmail.get('name')
  }
  get dateUser(){
    return this.userEmail.get('date')
  }
  get CVVNumber(){
    return this.userEmail.get('CVV')
  }
  get postalCode(){
    return this.userEmail.get('postalCode')
  }
  get direction(){
    return this.userEmail.get('direction')
  }

  buyProduct(){
    this.showAlertRequired = false;
    this.showAlertInvalidName = false;
    this.showAlertInvalidEmail = false;
    this.showAlertInvalidCard = false;
    this.showAlertInvalidCVV = false;
    this.showAlertInvalidPostalCode = false;
    this.showAlertInvalidDirection= false;
    this.showAlertInvalidDate = false;

    if (this.emailUser!.errors?.required || this.nameUser!.errors?.required || this.emailUser!.errors?.pattern || this.dateUser!.errors?.required || this.CVVNumber!.errors?.required || this.direction!.errors?.required ){
      this.showAlertRequired = true;
    } else if (this.emailUser!.errors?.pattern) {
      this.showAlertInvalidEmail = true;
    } else if (this.nameUser!.errors?.pattern) {
      this.showAlertInvalidName = true;
    } else if(this.dateUser!.errors?.pattern){
      this.showAlertInvalidDirection= true;
    } else if(this.cardUser!.errors?.pattern){
      this.showAlertInvalidCard = true;
    } else if(this.CVVNumber!.errors?.pattern){
      this.showAlertInvalidCVV = true;
    } else if(this.postalCode!.errors?.pattern){
      this.showAlertInvalidPostalCode = true;
    } else if(this.direction!.errors?.pattern){
      this.showAlertInvalidDirection= true;
    } else{
      const path = environment.path + `/api/buy/` + this.data.idProduct + "/" + this.token

      axios.post(path)
        .then((res) => {
          this.dialogRef.close();
          this.router.navigateByUrl('/', {skipLocationChange: true}).then(()=>
            this.router.navigate(['/products']));
        })
        .catch((error) => {
          alert(error.response.data.message)
        })
      this.dialogRef.close();
    }
  }


}
