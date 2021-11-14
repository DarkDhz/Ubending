import { Component, OnInit ,Inject} from '@angular/core';
import axios from 'axios'
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
  token = "null";

  constructor(public dialog: MatDialog) {
  }

  ngOnInit() {
    const currentUser = JSON.parse(<string>localStorage.getItem('currentUser'));
    if (currentUser != null) {
      this.token = currentUser.token;
    } else {
      //RETURN TO HOME
    }

    this.getProducts()
  }

  getProducts(){

    const path = 'http://127.0.0.1:5000/myproducts/' + this.token
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
  token = "null";
  constructor(

    public dialogRef: MatDialogRef<DialogContentExampleDialog>,
    @Inject(MAT_DIALOG_DATA) public data: DialogData) {
    const currentUser = JSON.parse(<string>localStorage.getItem('currentUser'));
    if (currentUser != null) {
      this.token = currentUser.token;
    } else {
      //RETURN TO HOME
    }
  }

  onNoClick(): void {
    this.dialogRef.close();
  }
  onYesClick(): void {
    // TODO auto update list of products
    const path = `http://127.0.0.1:5000/myproduct/` + this.data.idProduct + "/" + this.token
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



