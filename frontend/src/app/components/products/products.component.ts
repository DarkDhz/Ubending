import {AfterViewInit, Component, Inject, OnInit} from '@angular/core';
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
  category = 0
  params = {}
  name = ''
  wishlist = {products: []}
  isInWishlist = false;
  products_id = [];

  constructor(public dialog: MatDialog,private router: Router) {
    const currentUser = JSON.parse(<string>localStorage.getItem('currentUser'));
    if (currentUser != null) {
      this.token = currentUser.token;
      this.isLogged = true;
    }

  }

  ngOnInit(): void {
    //this.getProducts()
    //this.getProductsWishlist()

    const search = document.getElementById("search"); //pass the id of the input of searchbar
    try{
      this.category = JSON.parse(<string>localStorage.getItem('category'));
    }
    catch (error){
    }
    try{
      this.name = JSON.parse(<string>localStorage.getItem('nameSearch'));
      localStorage.setItem('nameSearch', JSON.stringify(''));
      // @ts-ignore
      search.value = this.name
    }
    catch (error){
    }
    this.getProducts(this.category)


    const products = document.getElementsByClassName("product_name")
    const btns = document.querySelectorAll('.btn');
    const storeProducts = document.getElementsByClassName("product_card")
    // @ts-ignore
    if(btns[1].innerText == "All"){
      btns[this.category + 1].classList.add('active');
    }
    else{
      btns[this.category].classList.add('active');

    }

    for (let i = 0; i < btns.length; i++) {

      btns[i].addEventListener('click', (e) => {
        // @ts-ignore
        if(btns[1].innerText == "All"){
          localStorage.setItem('category', JSON.stringify(i-1));
        }
        else{
          localStorage.setItem('category', JSON.stringify(i));

        }
        window.location.reload();

      });
    }
  }

  wishlistAnimation(num: number) {
    if (!this.isLogged) {
      this.loginRequiered()
    } else {
      const heart = document.getElementById('heart-'+num);
      //const like = document.getElementById('liketext-'+num);
      const click = heart!.classList.toggle('press');
      //like!.classList.toggle('press');

      if (click) {
        this.follow(num)
      } else {
        this.unfollow(num)
      }
    }
  }

  follow(id: number) {
    const path = environment.path + '/api/wishlist/' + this.token + "/" + id
    axios.post(path)
      .then((res) => {
      })
      .catch((error) => {
        console.error(error)
      })
  }

  unfollow(id: number) {
    const path = environment.path + '/api/wishlist/' + this.token + "/" + id
    axios.delete(path)
      .then((res) => {
      })
      .catch((error) => {
        console.error(error)
      })
  }

  isFollowing(id: number, value: boolean) {
    if (value) {
      return ['press']
    }
    return []
  }

  loginRequiered() {
    this.router.navigate(['/login-signup']);
  }

  searchByName(){
    const search = document.getElementById("search"); //pass the id of the input of searchbar
    // @ts-ignore
    localStorage.setItem('nameSearch', JSON.stringify(search.value));
    window.location.reload();


  }

  getProducts(category:number){

    const path = environment.path + '/api/search/' + this.token
    if(this.category == 0){
      this.params = {
        name: this.name,
        from: 0,
        jump: 20
      }
    }
    else{
      this.params = {
        name: this.name,
        from: 0,
        jump: 20,
        category: category
      }
    }
    console.log(category)

    axios.post(path, this.params)
      .then((res) => {
        // @ts-ignore
        this.state.products = res.data
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
    if (this.isLogged) {
      const dialogRef = this.dialog.open(Payment, {panelClass: 'custom-modalbox',
      data: {idProduct: idProduct,nameProduct: nameProduct,priceProduct:priceProduct, descProduct:descProduct,image: imagePath}});

      dialogRef.afterClosed().subscribe(result => {

      });
    } else {
      this.router.navigate(['/login-signup'])
    }

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
        Validators.pattern("^[a-zA-Z0-9 ]{2,100}$")])
    }
  );

  showAlertInvalidEmail = false;
  showAlertInvalidName = false;
  showAlertInvalidCard = false;
  showAlertInvalidDate = false;
  showAlertInvalidCVV = false;
  showAlertInvalidPostalCode = false;
  showAlertInvalidDirection = false;
  showAlertRequired = false;

  token = "null";

  constructor(
    public dialogRef: MatDialogRef<Payment>,
    @Inject(MAT_DIALOG_DATA) public data: DialogData, private uploadService: UploadService,
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

  get emailUser() {
    return this.userEmail.get('email')
  }

  get cardUser() {
    return this.userEmail.get('cardNumber')
  }

  get nameUser() {
    return this.userEmail.get('name')
  }

  get dateUser() {
    return this.userEmail.get('date')
  }

  get CVVNumber() {
    return this.userEmail.get('CVV')
  }

  get postalCode() {
    return this.userEmail.get('postalCode')
  }

  get direction() {
    return this.userEmail.get('direction')
  }

  buyProduct() {
    this.showAlertRequired = false;
    this.showAlertInvalidName = false;
    this.showAlertInvalidEmail = false;
    this.showAlertInvalidCard = false;
    this.showAlertInvalidCVV = false;
    this.showAlertInvalidPostalCode = false;
    this.showAlertInvalidDirection = false;
    this.showAlertInvalidDate = false;

    if (this.emailUser!.errors?.required || this.nameUser!.errors?.required || this.emailUser!.errors?.pattern || this.dateUser!.errors?.required || this.CVVNumber!.errors?.required || this.direction!.errors?.required) {
      this.showAlertRequired = true;
    } else if (this.emailUser!.errors?.pattern) {
      this.showAlertInvalidEmail = true;
    } else if (this.nameUser!.errors?.pattern) {
      this.showAlertInvalidName = true;
    } else if (this.dateUser!.errors?.pattern) {
      this.showAlertInvalidDirection = true;
    } else if (this.cardUser!.errors?.pattern) {
      this.showAlertInvalidCard = true;
    } else if (this.CVVNumber!.errors?.pattern) {
      this.showAlertInvalidCVV = true;
    } else if (this.postalCode!.errors?.pattern) {
      this.showAlertInvalidPostalCode = true;
    } else if (this.direction!.errors?.pattern) {
      this.showAlertInvalidDirection = true;
    } else {
      const path = environment.path + `/api/buy/` + this.data.idProduct + "/" + this.token

      axios.post(path)
        .then((res) => {
          this.dialogRef.close();
          this.router.navigateByUrl('/', {skipLocationChange: true}).then(() =>
            this.router.navigate(['/products']));
        })
        .catch((error) => {
          alert(error.response.data.message)
        })
      this.dialogRef.close();
    }
  }
}
