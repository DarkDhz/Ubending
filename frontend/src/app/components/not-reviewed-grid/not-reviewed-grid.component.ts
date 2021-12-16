import { Component, OnInit } from '@angular/core';
import {RatingComponent} from "../rating/rating.component";
import {MatDialog} from "@angular/material/dialog";

@Component({
  selector: 'app-not-reviewed-grid',
  templateUrl: './not-reviewed-grid.component.html',
  styleUrls: ['./not-reviewed-grid.component.css']
})
export class NotReviewedGridComponent implements OnInit {

  constructor(public dialog: MatDialog) { }

  ngOnInit(): void {
  }

  openRatingDialog(){
    this.dialog.open(RatingComponent);
  }
}
