import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NotReviewedGridComponent } from './not-reviewed-grid.component';

describe('NotReviewedGridComponent', () => {
  let component: NotReviewedGridComponent;
  let fixture: ComponentFixture<NotReviewedGridComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NotReviewedGridComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(NotReviewedGridComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
