import { Component, OnInit ,Inject} from '@angular/core';
import axios from 'axios'
import {MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material/dialog';
import {Router} from "@angular/router";
import {UploadService} from "../../services/upload.service";

export interface DialogData {
  idProduct: Number;
  nameProduct: string;
  image: string;
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

  constructor(public dialog: MatDialog, private router: Router) {
  }

  ngOnInit() {
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

    const path = 'http://127.0.0.1:5000/myproducts/' + this.token
    axios.get(path)
      .then((res) => {
        // @ts-ignore
        this.state.products = res.data
        console.log(res.data)
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

  loadProductImg(id: String) {
    this.url = "https://ubending.s3.eu-west-3.amazonaws.com/Captura.PNG";
  }

  openDialogDelete(nameProduct:String, idProduct:Number, imagePath:String) {
    const dialogRef = this.dialog.open(DialogContentExampleDialog, {
      data: {idProduct: idProduct,nameProduct: nameProduct, image: imagePath}
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
      console.log(result)
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
  constructor(public dialogRef: MatDialogRef<DialogContentExampleDialog>,
              @Inject(MAT_DIALOG_DATA) public data: DialogData,
              private uploadService: UploadService,
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
    this.dialogRef.close("here the result");
  }
  onYesClick(): void {
    console.log("product"+this.data.idProduct+"."+this.data.image)
    const path = `http://127.0.0.1:5000/myproduct/` + this.data.idProduct + "/" + this.token
    axios.delete(path)
      .then((res) => {
        this.uploadService.deleteFile("product"+this.data.idProduct+"."+this.data.image)
        alert('PRODUCT DELETE CORRECTLY')
        this.router.navigateByUrl('/', {skipLocationChange: true}).then(()=>
          this.router.navigate(['/user-products']));
      })
      .catch((error) => {
        console.error(error)
        alert('ERROR DELETING PRODUCT')
      })
    this.dialogRef.close();

  }
}



