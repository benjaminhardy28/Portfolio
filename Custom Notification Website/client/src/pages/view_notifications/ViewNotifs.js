import "./ViewNotifs.css"
import NotifsBox from './NotifsBox'
import axios from '../../api/axios.js';
import useAuth from '../../hooks/useAuth';
import { useState, useEffect } from 'react'

const SET_NOTIF_URL = "set_notification";

const ViewNotifs = () =>  {
    const { auth } = useAuth();

    const [userNotifs, setUserNotifs] = useState([])


    useEffect(() => {
        requestSetNotifications();
    }, []);

    const requestSetNotifications = async () => {
        try{
            const response = await axios.get(
                SET_NOTIF_URL,
                {
                  headers: { 'Content-Type': 'application/json', 'x-access-token': auth.accessToken },
                  withCredentials: true 
                }
              ); 
            console.log(JSON.stringify(response));
            setUserNotifs(response.data.SetNotification);
        }catch(err){
            console.log("Could not get Notifications");
        }
    }

    const getFilteredSearch = (notifQuery, notifs) => {
        if (!notifQuery){
            return notifs
        }
        return notifs.filter(notif => notif.website_url.toLowerCase().includes(notifQuery.toLowerCase()))
    }

    const [notifQuery, setNotifQuery] = useState('');
    const filteredNotifs = getFilteredSearch(notifQuery, userNotifs)


    return (
        <div className = "viewNotifs">
            <h1 className = "specificPageTitle">
                View Your Own Custom Notifications
            </h1>
            <div className="searchBarContainer">
                <div className="inputGroup">
                    <input type="text" id="search" className="searchBar inputGroup__input" onChange={e => setNotifQuery(e.target.value)} required  />
                    <label htmlFor="search" className="inputGroup__label"> Search For A Notification </label>
                </div>
            </div>
            <NotifsBox props={filteredNotifs}/>
        </div>
    )
}

export default ViewNotifs;