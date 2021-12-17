import { Component, OnInit } from '@angular/core';
import {RatingComponent} from "../rating/rating.component";
import {MatDialog} from "@angular/material/dialog";
import {environment} from "../../enviroment";
import axios from "axios";

@Component({
  selector: 'app-not-reviewed-grid',
  templateUrl: './not-reviewed-grid.component.html',
  styleUrls: ['./not-reviewed-grid.component.css']
})
export class NotReviewedGridComponent implements OnInit {

  token = "null";
  isLogged = false;
  state = {products: []}

  constructor(public dialog: MatDialog) {
    const currentUser = JSON.parse(<string>localStorage.getItem('currentUser'));
    if (currentUser != null) {
      this.token = currentUser.token;
      this.isLogged = true;
    } else {

    }
    this.getProducts()
  }

  ngOnInit(): void {
  }

  openRatingDialog(id: number){
    this.dialog.open(RatingComponent, {data: id});
  }

  getProducts(){

    const path = environment.path + '/api/to_rate/' + this.token

    axios.get(path)
      .then((res) => {
        // @ts-ignore
        this.state.products = res.data
      })
      .catch((error) => {
        console.error(error)
      })
  }

}
