import { Routes } from '@angular/router';

export const routes: Routes = [
    {
        path: 'awardsearch',
        loadComponent: () => import('./award-search/award-search/award-search.component').then((c) => c.AwardSearchComponent),
    }
];
