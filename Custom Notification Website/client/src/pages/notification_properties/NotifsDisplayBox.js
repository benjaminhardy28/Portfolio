import EachNotifCard from "./EachNotifCard.js"
//import "./NotifsDisplayBox.css"

const NotifsDisplayBox = ( {props} ) => {
    const reversedProps = Array.isArray(props) ? [...props].reverse() : [];

    return(
        <div className="notifsDisplayBox">
                {/* {props.map((notification) => (
                    <EachNotifCard props={notification} key={notification.id}/> 
                ))} */}
                {reversedProps.length > 0 ? (
                reversedProps.map((notification) => (
                    <EachNotifCard props={notification} key={notification.id} />
                ))
                ) : (
                    <div>No data to display.</div>
                )}
        </div>
    );
};

export default NotifsDisplayBox;