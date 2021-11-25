import { Component, OnInit ,Inject} from '@angular/core';
import axios from 'axios'
import {MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material/dialog';
import {Router} from "@angular/router";
import {UploadService} from "../../services/upload.service";

export interface DialogData {
  idProduct: Number;
  nameProduct: string;
  priceProduct: string;
  descProduct: string;
  category: Number;
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
      })
      .catch((error) => {
        console.error(error)
      })
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
  openDialogEdit(nameProduct:String,idProduct:Number,priceProduct:Number,descProduct:String,category:Number) {
    const dialogRef = this.dialog.open(DialogEdit, {panelClass: 'custom-modalbox',
      data: {idProduct: idProduct,nameProduct: nameProduct, priceProduct:priceProduct, descProduct:descProduct,category:category}
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
    });
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

@Component({
  selector: 'dialog-edit',
  templateUrl: 'dialog-edit.html',
  styleUrls: ['dialog-edit.css']
})
export class DialogEdit {
  category_id: Number = -1;
  state_id: Number = -1;

  state = {categories: []};
  params = {};
  idProduct:Number = 0;
  selectedFiles : FileList | undefined;
  constructor(
    public dialogRef: MatDialogRef<DialogEdit>,
    @Inject(MAT_DIALOG_DATA) public data: DialogData) {
    this.idProduct = data.idProduct;
    const path = 'http://127.0.0.1:5000/categories'
    axios.get(path)
      .then((res) => {

        // @ts-ignore
        this.state.categories =  res.data
      })
      .catch((error) => {
        console.error(error)
      })
    this.category_id = data.category
  }

  onNoClick(): void {
    this.dialogRef.close();
  }

  selectCategory(event: any) {
    this.category_id = (<HTMLSelectElement>event.target).selectedIndex;
  }
  selectState(event: any) {
    this.state_id = (<HTMLSelectElement>event.target).selectedIndex;
  }

  selectFile(event: any) {
    this.selectedFiles = event.target.files;
  }

  onYesClick(): void {
    console.log((<HTMLSelectElement>document.getElementById("product_state")).value)
    let product_name = (<HTMLInputElement>document.getElementById("input_name")).value;
    let product_price = (<HTMLInputElement>document.getElementById("input_price")).value;

    let product_category = (<HTMLSelectElement>document.getElementById("product_category")).selectedIndex;
    let product_desc = (<HTMLInputElement>document.getElementById("input_desc")).value;
    if (!product_name || !product_price || !product_desc || this.category_id == -1 || this.selectedFiles == undefined) {
      alert("invalid params")
      this.params = {
        name: product_name,
        description: product_desc,
        price: product_price,
        product_category: this.category_id,
        product_state: this.state_id,
        // @ts-ignore
        image: this.selectedFiles.item(0).type.split('/').pop(),
        category_id: this.category_id
      }
      console.log(this.params)
      alert("PAUSA")
    } else {
      // @ts-ignore
      this.params = {
        name: product_name,
        description: product_desc,
        price: product_price,
        product_category: this.category_id,
        product_state: this.state_id,
        // @ts-ignore
        image: this.selectedFiles.item(0).type.split('/').pop(),
        category_id: this.category_id
      }
    }
    console.log(this.params)
    alert("PAUSA")
    /*
    const path = "https://ubending3.herokuapp.com/user/1/product/+ this.data.idProduct"
    axios.delete(path)
      .then((res) => {
        alert('PRODUCT DELETE CORRECTLY')
      })
      .catch((error) => {
        console.error(error)
        alert('ERROR AL DELETE PRODUCT')
      })
    this.dialogRef.close();

     */
  }
}



