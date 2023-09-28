import AccountInfo from '../pages/account_information/AccountInfo';
import ViewNotifs from '../pages/view_notifications/ViewNotifs';
import NotifProps from '../pages/notification_properties/NotifProps';
import Home from '../pages/home/Home';
import Login from '../pages/login/Login';
import SignUp from '../pages/sign_up/SignUp';
import '../components_css/TextBox.css';
import '../components_css/Button.css';
import Layout from './Layout.js';
import RequireAuth from './RequireAuth.js'
import React, { useState, useEffect, useRef } from 'react';
import { Route, Routes} from 'react-router-dom';


const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Layout />} >
        {/*public routes*/}
        <Route path="/login" element={<Login />} />
        <Route path="/sign-up" element={<SignUp />} />
        {/*private routes*/}
        <Route element={<RequireAuth />}>
        <Route path="/view-notifications" element={<ViewNotifs />} />
          <Route path="/account-information" element={<AccountInfo />} />
          <Route path="/view-notifications/noficiation-properties/:id" element={<NotifProps/>} />
        </Route>
      </Route>
    </Routes>
  );
}

export default App;

