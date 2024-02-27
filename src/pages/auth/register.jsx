import { Link } from 'react-router-dom';
import { PatternFormat } from 'react-number-format';
import { useEffect, useState } from 'react';
import './style.css';
import ReactLoading from 'react-loading';
import { ToastContainer, toast } from 'react-toastify';
import axios from 'axios';
import { useDispatch } from 'react-redux';
import { setSignInSuccess } from '../../store/auth/sessionSlice';

function validatePassword(password) {
    // Define the criteria for a valid password
    const minLength = 6;
    const maxLength = 20;
    const hasUppercase = /[A-Z]/.test(password);
    const hasLowercase = /[a-z]/.test(password);
    const hasNumber = /\d/.test(password);
    const hasSpecialChar = /[!@#$%^&*(),.?":{}|<>]/.test(password);

    // Check if the password meets all criteria
    if (
        password.length >= minLength &&
        password.length <= maxLength &&
        hasUppercase &&
        hasLowercase &&
        hasNumber &&
        hasSpecialChar
    ) {
        return true;
    } else {
        return false;
    }
}

export default function Register() {
    const [phoneNumber, setPhoneNumber] = useState('');
    const [name, setName] = useState('');
    const [lastname, setLastname] = useState('');
	const [password, setPassword] = useState('');
    const [confirmPass, setConfirmPass] = useState('');
    const [showLoading, setShowLoading] = useState(false);

    const [isValidForm, setIsValidForm] = useState(false);

    const dispatch = useDispatch();

    useEffect(() => {
        const isPasswordValid = validatePassword(password);
        const isPasswordsEqual = password === confirmPass;
        const isValidName = name.length >= 4;
        const isValidPhoneNumber = phoneNumber.replace(/[^0-9]/g,"").length === 12;
        setIsValidForm(isPasswordValid && isPasswordsEqual && isValidName && isValidPhoneNumber)

    }, [phoneNumber, name, password, confirmPass]);

    const handleSubmit = (e) => {
        e.preventDefault();
        const formattedPhoneNumber = phoneNumber.replace(/\s|\(|\)/g, '');
        setShowLoading(true);

        axios.post('https://educationsapi.pythonanywhere.com/accounts/register/', {
                phone: formattedPhoneNumber,
                password: password,
                password2: confirmPass,
                first_name: name
        })
        .then(res => {
            setShowLoading(false);
            toast.info("Siz muvaffaqqiyatli ro'yxatdan o'ttingiz!");
            dispatch(setSignInSuccess(res.data.access_token))
        })
        .catch(err => {
            setShowLoading(false);
            toast.info("Siz muvaffaqqiyatli ro'yxatdan o'tmadingiz!");
        })
    };

    return (
        <div className="container-fluid">
            <div className="row">
    
                <div className="col-lg-6 col-md-6 infinity-form-container loading">		
                    <ToastContainer />
			
                    <div className="col-lg-9 col-md-12 col-sm-8 col-xs-12 infinity-form">
                        <div className="text-center mb-3 mt-5">
                            {/* <img src="logo.png" width="150px"> */}
                        </div>
                        <div className="text-center mb-4">
                            <h4>Ro'yxatdan o'tish</h4>
                        </div>
                        <form className="px-3" onSubmit={handleSubmit}>
                            <div className="form-input">
                                <span><i style={{fontSize: '18px'}} className="fa fa-phone"></i></span>
							    <PatternFormat onChange={(e) => setPhoneNumber(e.target.value)} tabIndex="10" format="+998 (##) ### ## ##" placeholder="+998" valueIsNumericString={true} />
                                <div className="bottom-line"></div>
                            </div>
                            {/* Name  */}
                            <div className="form-input">
                                <span><i className="fa fa-user"></i></span>
                                <input value={name} onChange={e => setName(e.target.value)} type="text" name="" placeholder="Ismingizni kiriting" required />
                                <div className="bottom-line"></div>
                            </div>
                             {/* Lastname  */}
                             {/* <div className="form-input">
                                <span><i className="fa fa-user"></i></span>
                                <input value={lastname} onChange={e => setLastname(e.target.value)} type="text" name="" placeholder="Familiyangizni kiriting" required />
                                <div className="bottom-line"></div>
                            </div> */}
                            {/* Password */}
                            <div className="form-input">
                                <span><i className="fa fa-lock"></i></span>
                                <input value={password} onChange={e => setPassword(e.target.value)} type="password" name="" placeholder="Parol" required />
                                <div className="bottom-line"></div>
                            </div>
                            {/* Confirm Password */}
                            <div className="form-input">
                                <span><i className="fa fa-lock"></i></span>
                                <input value={confirmPass} onChange={e => setConfirmPass(e.target.value)} type="password" name="" placeholder="Parol tastig'i" required />
                                <div className="bottom-line"></div>
                            </div>
                            {/* Submit Button */}
                            <div className="mb-3 mt-5"> 
                                <button type="submit" disabled={!isValidForm} className="btn btn-block">Ro'yxatdan o'tish</button>
                            </div>
                            {/* <div className="text-center mb-2">
                                 <div className="text-center mb-3" style={{color: '#777'}}>or login with</div>
                                <a href="" className="btn btn-social btn-facebook">facebook</a>
    
                                <a href="" className="btn btn-social btn-google">google</a>
    
                                <a href="" className="btn btn-social btn-twitter">twitter</a>
                            </div> */}
                            <div className="text-center mb-5 mt-2" style={{color: '#777'}}>
                                <p>
                                    Men allaqachon ro'yhatdan o'tganman 
                                </p>
                                <Link className="login-link" to='/login'> Kirish</Link>
                           </div>
                        </form>
                    </div>
                    <div className={`loading-container ${showLoading ? 'd-block' : 'd-none'}`}>
					<ReactLoading className="react-loading" color="blue" type="spin" />
				</div>
                </div>



                <div className="col-lg-6 col-md-6 d-none d-md-block infinity-image-container"></div>

            </div>
        </div>	
    );
}