import { Component, OnInit } from '@angular/core';
import { faFilter,faStar,faComments,faClipboardList,faIdBadge} from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.css']
})

export class SearchBarComponent implements OnInit {
  faFilter = faFilter;
  faStar = faStar;
  faIdBadge = faIdBadge;
  faComments = faComments;
  faClipboardList = faClipboardList;



  constructor() { }

  ngOnInit(): void {
  }

  search(){
    alert('Implement search...')
  }

  filters(){
    alert('Implement filters...')
  }

  liked(){
    alert('Implement liked...')
  }

  chat(){
    alert('Implement chat...')
  }
  products(){
    alert('Implement products...')
  }
  profile(){
    alert('Implement profile...')
  }


}
