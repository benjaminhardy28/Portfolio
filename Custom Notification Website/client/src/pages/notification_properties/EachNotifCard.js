const EachNotifCard = ( { props } ) => {
    return (
        <ul className="eachNotifCard">
                {/*<p> {props.Date/Time} </p>*/}
                <p> {props.full_notification}</p>
                <p> Prompt: {props.notif_description} </p>
        </ul>
    );
};

export default EachNotifCard;