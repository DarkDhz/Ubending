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
    let star5 = (<HTMLInputElement>document.getElementById("star5")).value;
    if (star5 == 'on') {
      return 5
    } else {
      let star4 = (<HTMLInputElement>document.getElementById("star4")).value;
      if (star4 == 'on') {
        return 4
      } else {
        let star3 = (<HTMLInputElement>document.getElementById("star3")).value;
        if (star3 == 'on') {
          return 3
        } else {
          let star2 = (<HTMLInputElement>document.getElementById("star2")).value;
          if (star2 == 'on') {
            return 2
          } else {
            return 1
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
