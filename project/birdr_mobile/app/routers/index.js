import Vue from 'nativescript-vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const router = new VueRouter({
    pageRouting: true,
    routes: [
        {
          path: '/home',
          component: Home,
          meta: {
            title: 'Home',
          },
        },
        {path: '*', redirect: '/home'},
    ],
});


router.replace('/home');

module.exports = router;
