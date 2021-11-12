import { Component, OnInit ,Inject} from '@angular/core';
import axios from 'axios'
import {AppComponent} from "../../app.component";
import {MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material/dialog';
export interface DialogData {
  idProduct: Number;
  nameProduct: string;
}
@Component({
  selector: 'app-user-products',
  templateUrl: './user-products.component.html',
  styleUrls: ['./user-products.component.css']
})

export class UserProductsComponent implements OnInit{
  title = 'frontend';
  name: string | undefined;
  state = {products: []}
  constructor(public dialog: MatDialog) {
    this.getProducts()
  }

  ngOnInit() {
  }
  getProducts(){
    const path = 'https://ubending3.herokuapp.com/myproducts'
    axios.get(path)
      .then((res) => {
        // @ts-ignore
        this.state.products =  res.data
        console.log(this.state.products)
      })
      .catch((error) => {
        console.error(error)
      })
  }
  url:string = "/images/sneaker.jpg"
  url1:string = "../images/img2.jpg"
  url2:string = "../images/img2.jpg"
  url3:string = "../images/img2.jpg"
  url4:string = "../images/img2.jpg"

  changeImage(event:any){
    this.url = event.target.src;
  }

  changeImage1(event:any){
    this.url1 = event.target.src;
  }

  changeImage2(event:any){
    this.url2 = event.target.src;
  }

  changeImage3(event:any){
    this.url3 = event.target.src;
  }

  changeImage4(event:any){
    this.url4 = event.target.src;
  }
  openDialogDelete(nameProduct:String,idProduct:Number) {
    const dialogRef = this.dialog.open(DialogContentExampleDialog, {
      data: {idProduct: idProduct,nameProduct: nameProduct}
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
    });
  }
  openDialogEdit(nameProduct:String,idProduct:Number) {

  }
}

@Component({
  selector: 'dialog-content-example-dialog',
  templateUrl: 'dialog-content-example-dialog.html',
  styleUrls: ['dialog-content-example-dialog.css']
})
export class DialogContentExampleDialog {
  constructor(
    public dialogRef: MatDialogRef<DialogContentExampleDialog>,
    @Inject(MAT_DIALOG_DATA) public data: DialogData) {}

  onNoClick(): void {
    this.dialogRef.close();
  }
  onYesClick(): void {
    const path = `https://ubending3.herokuapp.com/user/1/product/`+ this.data.idProduct
    axios.delete(path)
      .then((res) => {
        alert('PRODUCT DELETE CORRECTLY')
      })
      .catch((error) => {
        console.error(error)
        alert('ERROR AL DELETE PRODUCT')
      })
    this.dialogRef.close();
  }
}



