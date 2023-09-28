import { useState, useRef, useEffect } from 'react';
import { Link, useNavigate, useLocation } from "react-router-dom";
import axios from '../../api/axios.js';

const SIGNUP_URL = '/user';

const SignUpBox = () => {
    const navigate = useNavigate();
    const location = useLocation();
    const from = location.state?.from?.pathname || "/";
    
    const errRef = useRef();
    const [errMsg, setErrMsg] = useState('');
    const [success, setSuccess] = useState(false);
    const [newEmail, setNewEmail] = useState('');
    const [newPassword, setNewPassword] = useState('');
    const [newPhoneNumber, setNewPhoneNumber] = useState('');

    const handleInputChange = (event) => {
        setNewEmail(event.target.value);
    };

    const handleSubmit = async (e) => {
        e.preventDefault()
        try {
            const response = await axios.post(
                SIGNUP_URL,
                JSON.stringify({
                  email: newEmail,
                  phone_number: newPhoneNumber,
                  password: newPassword,
                }),
                {
                  headers: { 'Content-Type': 'application/json' },
                  withCredentials: true // Set credentials option here
                }
              );   
              setErrMsg('')     
              navigate(from, { replace: true });
              console.log(JSON.stringify(response))
              navigate(from, { replace: true });
        } catch (err){
            if (!err?.response) {
                setErrMsg('No Server Reponse');
            } else if (err.reponse?.status == 409) {
                setErrMsg('Username Taken')
            } else {
                setErrMsg('Registration Failed')
            }
            errRef.current.focus();
        }
    }

    return(
        <>
        { success ? (
            <section>
                <h1>Success</h1>
            </section>
        ) : (
            <section className="signUpBox">
                <p ref={errRef} className={errMsg ? "errmsg" : "offscreen"} aria-live="asserive">
                    {errMsg}
                </p>
                <h1>
                    Please Sign Up
                </h1>
                <p>
                    This contact information will be used for any of your notifications.
                </p>
                <form onSubmit={handleSubmit}>
                    <div className="inputContainer">
                        <div className="inputGroup">
                            <input type="text" id="newEmail" autoComplete="off" className="authorizeInput inputGroup__input" required onChange={(newEmail => setNewEmail(newEmail.target.value))}/>
                            <label htmlFor="newEmail" className="inputGroup__label">
                                Email Address
                            </label>
                        </div>
                        <div className="inputGroup">
                            <input type="text" id="newPhoneNumber" autoComplete="off" className="authorizeInput inputGroup__input" required  onChange={(newPhoneNumber => setNewPhoneNumber(newPhoneNumber.target.value))}/>
                            <label htmlFor="newPhoneNumber" className="inputGroup__label">
                                Phone Number
                            </label>
                        </div>
                        <div className="inputGroup">
                            <input type="password" id="newPassword" className="authorizeInput inputGroup__input" required onChange={(newPassword => setNewPassword(newPassword.target.value))}  />
                            <label htmlFor="newPassword" className="inputGroup__label">
                                Password
                            </label>
                        </div>
                    </div>
                    <div className="buttonContainer">
                        <button className="button">
                            Sign Up
                        </button>
                    </div>
                </form>
                <p>
                    Already gave an account? <Link to="/login">Log In Now</Link>
                </p>
            </section>
            )}
        </>
    );
};

export default SignUpBox