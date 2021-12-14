import {Component, OnInit} from '@angular/core';
import {Router} from "@angular/router";
import axios from "axios";
import {environment} from "../../enviroment";
import {MatDialog} from "@angular/material/dialog";
import {Payment} from "../products/products.component";



@Component({
  selector: 'app-wishlist',
  templateUrl: './wishlist.component.html',
  styleUrls: ['./wishlist.component.css']
})
export class WishlistComponent implements OnInit {

  isLogged = false;
  token = "null";
  state = {products: []}
  isEmpty = false;

  constructor(public dialog: MatDialog,private router: Router) {
  }

  ngOnInit(): void {
    const currentUser = JSON.parse(<string>localStorage.getItem('currentUser'));
    if (currentUser != null) {
      this.token = currentUser.token;
    } else {
      alert('NOT LOGGED IN')
      this.router.navigate(['/home']);
    }

    this.getProducts()
  }

  getProducts(){
    const path = environment.path + '/api/wishlist/' + this.token
    axios.get(path)
      .then((res) => {
        this.isEmpty = false
        // @ts-ignore
        this.state.products = res.data
        console.log("WISHLIST: ", res.data)
      })
      .catch((error) => {
        this.isEmpty = true
        console.error(error)
      })
  }

  loginRequiered() {
    this.router.navigate(['/login-signup']);
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

  delete(id: Number): void {
    const path = environment.path + '/api/wishlist/' + this.token + "/" + id
    axios.delete(path)
      .then((res) => {
        this.router.navigateByUrl('/', {skipLocationChange: true}).then(()=>
          this.router.navigate(['/wishlist']));
      })
      .catch((error) => {
        console.error(error)
      })
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
