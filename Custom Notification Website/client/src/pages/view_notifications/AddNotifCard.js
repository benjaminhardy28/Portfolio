//import "./AddNotifCard.css"
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPlus } from "@fortawesome/free-solid-svg-icons";


const AddNotifCard = () => {

    return (
        <div  >
            <ul>
                <div className = "customIcon">
                    <FontAwesomeIcon icon={faPlus}style={{color: "#1eff00",}} />
                </div>
                <p> Add New Custom Notification </p>
            </ul>
        </div>
    );
}

export default AddNotifCard