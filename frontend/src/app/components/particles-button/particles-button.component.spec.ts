import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ParticlesButtonComponent } from './particles-button.component';

describe('ParticlesButtonComponent', () => {
  let component: ParticlesButtonComponent;
  let fixture: ComponentFixture<ParticlesButtonComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ParticlesButtonComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ParticlesButtonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
