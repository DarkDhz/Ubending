import {Component, Inject, OnInit} from '@angular/core';
import {MAT_DIALOG_DATA, MatDialogRef} from "@angular/material/dialog";
import {environment} from "../../enviroment";
import axios from "axios";
import {Router} from "@angular/router";

@Component({
  selector: 'app-rating',
  templateUrl: './rating.component.html',
  styleUrls: ['./rating.component.css']
})
export class RatingComponent implements OnInit {
  token = "null";
  isLogged = false;

  constructor(public dialogRef: MatDialogRef<RatingComponent>,
              @Inject(MAT_DIALOG_DATA) public data: number,
              private router: Router) {
    const currentUser = JSON.parse(<string>localStorage.getItem('currentUser'));
    if (currentUser != null) {
      this.token = currentUser.token;
      this.isLogged = true;
    } else {

    }
  }

  ngOnInit(): void {
  }

  getRating() {
    let star5 = (<HTMLInputElement>document.getElementById("star1")).checked;
    if (star5) {
      return 5
    } else {
      let star4 = (<HTMLInputElement>document.getElementById("star2")).checked;
      if (star4) {
        return 4
      } else {
        let star3 = (<HTMLInputElement>document.getElementById("star3")).checked;
        if (star3) {
          return 3
        } else {
          let star2 = (<HTMLInputElement>document.getElementById("star4")).checked;
          if (star2) {
            return 2
          } else {
            let star1 = (<HTMLInputElement>document.getElementById("star5")).checked;
            if (star1) {
              return 1
            } else {
              return 0
            }
          }
        }
      }

    }
  }

  submitRating() {
    const path = environment.path + "/api/rate/" + this.data + "/" + this.token
    let value = this.getRating()
    const params = {
      'rating': value
    }

    axios.post(path, params)
      .then((res) => {
        this.dialogRef.close();
        this.router.navigateByUrl('/', {skipLocationChange: true}).then(()=>
          this.router.navigate(['/reviews']));
      })
      .catch((error) => {
        alert(error.response.data.message)
        this.dialogRef.close();
      })

  }

}
