import { Component, OnInit } from '@angular/core';
import {Router} from "@angular/router";
import {environment} from "../../enviroment";
import axios from "axios";

@Component({
  selector: 'app-reviewed-grid',
  templateUrl: './reviewed-grid.component.html',
  styleUrls: ['./reviewed-grid.component.css']
})
export class ReviewedGridComponent implements OnInit {

  token = "null";
  isLogged = false;
  state = {products: []}
  p = [1,2,3,4,5,6,7,8];
  ratings = {1: 2, 2: 3, 3: 4, 4: 4, 5: 5, 6: 3, 7: 4, 8: 3}

  constructor(private router: Router) {
    const currentUser = JSON.parse(<string>localStorage.getItem('currentUser'));
    if (currentUser != null) {
      this.token = currentUser.token;
      this.isLogged = true;
    } else {
      this.router.navigate(['/login-signup']);
    }
    this.getProducts()
  }

  ngOnInit(): void {
  }

  load = false;

  getProducts(){
    const path = environment.path + '/api/rated/' + this.token

    axios.get(path)
      .then((res) => {
        // @ts-ignore
        this.state.products = res.data
        this.representImages()
      })
      .catch((error) => {
        console.error(error)
      })
  }

  calculateWidth(val: number) {
    return String(40*Number(val)-15);
  }

  representImages() {
    for(let i in this.state.products) {
      console.log(i)
      // @ts-ignore
      document.getElementById('starts-inner-' + i['product_id'])!.style.width = String(40*Number(i['valoration'])-15);
      // @ts-ignore
      console.log(document.getElementById('starts-inner-' + i['product_id'])!.style.width);
      console.log('asd')
      // @ts-ignore
      console.log(i*100)
    }
  }

  ngAfterViewInit(): void{
    for(let i in this.state.products) {
      // @ts-ignore
      document.getElementById('starts-inner-' + i['product_id'])!.style.width = String(40*Number(i['valoration'])-15);
      // @ts-ignore
      console.log(document.getElementById('starts-inner-' + i['product_id'])!.style.width);
      console.log('asd')
      // @ts-ignore
      console.log(i*100)
    }
  }
}
