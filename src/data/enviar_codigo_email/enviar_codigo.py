import smtplib
import email.message
from src.doman.use_cases.enviar_codigo_email import (
    EnviarCodigoEmail as EnviarCodigoEmailInterface,
)


class EnviarCodigoEmail(EnviarCodigoEmailInterface):
    def enviar_email_codigo(self, codigo: int, email_destinatario: str) -> bool:
        """
        envio de email com o codigo de validação, para cadastrar.
        """
        try:
            corpo_email = f"<p>Seu código para validação é: {codigo}</p>"

            msg = email.message.Message()
            msg["Subject"] = "<h2>Validação de Email.</h2>"
            msg["From"] = f"tec.mundo.py@gmail.com"
            msg["To"] = f"{email_destinatario}"
            password = f"jakhonuthvdvrkvw"
            msg.add_header("Content-Type", "text/html")
            msg.set_payload(corpo_email)

            s = smtplib.SMTP("smtp.gmail.com: 587")
            s.starttls()

            s.login(msg["From"], password)
            s.sendmail(msg["from"], [msg["to"]], msg.as_string().encode("utf-8"))

            return {
                "Success": True,
                "Data": {"codigo_enviado": codigo, "Email": email_destinatario},
            }

        except:
            return {"Success": False, "Data": None}
