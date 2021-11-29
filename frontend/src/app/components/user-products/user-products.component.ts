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
  stateProduct: number;
  category: number;
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

    const path = 'https://ubending4.herokuapp.com/myproducts/' + this.token
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

  openDialogDelete(nameProduct:String, idProduct:Number, imagePath:String) {
    const dialogRef = this.dialog.open(DialogContentExampleDialog, {
      data: {idProduct: idProduct,nameProduct: nameProduct, image: imagePath}
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
      console.log(result)
    });
  }
  openDialogEdit(nameProduct:String,idProduct:Number,stateProduct: number,priceProduct:Number,descProduct:String,category:Number,imagePath:String) {
    const dialogRef = this.dialog.open(DialogEdit, {panelClass: 'custom-modalbox',
      data: {idProduct: idProduct,nameProduct: nameProduct,stateProduct : stateProduct, priceProduct:priceProduct, descProduct:descProduct,category:category,image: imagePath}
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
    const path = `https://ubending4.herokuapp.com/myproduct/` + this.data.idProduct + "/" + this.token
    axios.delete(path)
      .then((res) => {
        this.uploadService.deleteFile("product"+this.data.idProduct+"."+this.data.image)
        alert('PRODUCT DELETE CORRECTLY')
        this.router.navigateByUrl('/', {skipLocationChange: true}).then(()=>
          this.router.navigate(['/user-products']));
      })
      .catch((error) => {
        console.error(error)
        alert(error.response.data.message)
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
  token = "null";
  states = ["New","Worn out","Destroyed"];

  state = {categories: []};
  params = {};
  idProduct:Number = 0;
  selectedFiles : FileList | undefined;
  constructor(
    public dialogRef: MatDialogRef<DialogEdit>,
    @Inject(MAT_DIALOG_DATA) public data: DialogData,private uploadService: UploadService,
    private router: Router) {
    this.idProduct = data.idProduct;
    const path = 'https://ubending4.herokuapp.com/categories'
    axios.get(path)
      .then((res) => {
        console.log(res.data)
        // @ts-ignore
        this.state.categories =  res.data
      })
      .catch((error) => {
        console.error(error)
      })
    const currentUser = JSON.parse(<string>localStorage.getItem('currentUser'));
    if (currentUser != null) {
      this.token = currentUser.token;
    } else {
      alert('NOT LOGGED IN')
      this.router.navigate(['/home']);
    }
    this.category_id = data.category
    console.log(this.state.categories)
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
    } else {
      // @ts-ignore
      this.params = {
        token: this.token,
        name: product_name,
        description: product_desc,
        price: product_price,
        category_id: this.category_id,
        state: this.state_id,
        // @ts-ignore
        image: this.selectedFiles.item(0).type.split('/').pop()
      }

    console.log(this.params)
    const path = `https://ubending4.herokuapp.com/myproduct/` + this.data.idProduct + "/" + this.token
    axios.put(path,this.params)
      .then((res) => {
        //this.uploadService.deleteFile("product"+this.data.idProduct+"."+this.data.image)
        alert('PRODUCT EDIT CORRECTLY')
        this.router.navigateByUrl('/', {skipLocationChange: true}).then(()=>
          this.router.navigate(['/user-products']));
        this.dialogRef.close();
      })
      .catch((error) => {
        alert(error.response.data.message)
      })
  }
  }
}



