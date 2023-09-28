import { useParams } from 'react-router-dom';
import { useEffect, useState } from 'react';
import "./NotifProps.css";
import NotifSettings from "./NotifSettings.js";
import NotifsDisplayBox from "./NotifsDisplayBox.js";
import axios from '../../api/axios.js';
import useAuth from '../../hooks/useAuth';

const NOTIF_URL = '/notifications';

const NotifProps = () => {

    const { id } = useParams();

    const { auth } = useAuth();

    const [notifInfo, setNotifInfo] = useState([])

    useEffect(() => {
        requestNotifications();
    }, []);
    //id will be used to get information for notif
    // const id_info = [
    //     {
    //         notifications: [
    //              { 'Date/Time' : "7/15/23 02:53 PM", notif_description}
    //             { id: 1, date: "22/7", notification: "new post", prompt: "current" },
    //             { id: 2, date: "17/7", notification: "new post", prompt: "current" },
    //             { id: 3, date: "15/7", notification: "new post", prompt: "current" },
    //             { id: 4, date: "12/7", notification: "new post", prompt: "New Playlist" },
    //             { id: 5, date: "9/7", notification: "new post", prompt: "New Playlist" }
    //         ]
    //     }
    // ];


//     data = {}
//     data['Date/Time'] = notif.date_time
//     data['notif_description'] = notif.notif_description
//     data['full_notification'] = notif.full_notification
//     data['short_notification'] = notif.short_notification
//     notifs_content.append(data)
// if not all_notifications:
//     return jsonify({'message' : 'There are no notifications',  'user_id' : current_user.id, 'notif_id' : setNotif_id})
// return jsonify({'notifications' : notifs_content,  'user_id' : current_user.id, 'notif_id' : setNotif_id})

    /* API CALL
        get all * notifDate, fullNotif, notifPrompt
    */

    const requestNotifications = async () => {
        try{
            const response = await axios.get(
                NOTIF_URL + '/' + id,
                {
                    headers: { 'Content-Type': 'application/json', 'x-access-token': auth.accessToken },
                    withCredentials: true 
                }
                ); 
            console.log(JSON.stringify(response));
            setNotifInfo(response.data.notifications);
        }catch(err){
            console.log("Could not get Notifications");
        }
    }   

    return(
        <div className="notifProps">
            <h1 className="specificPageTitle">
                Your Custom Notification
            </h1>
            <div className="notifInfoContainer">
                {/*<NotifSettings props={notifInfo}/>*/}
                <NotifsDisplayBox props={notifInfo}/>
            </div>
        </div>
    )
};

export default NotifProps;