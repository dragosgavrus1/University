import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListGradesComponent } from './list-grades.component';

describe('ListGradesComponent', () => {
  let component: ListGradesComponent;
  let fixture: ComponentFixture<ListGradesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ListGradesComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ListGradesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
