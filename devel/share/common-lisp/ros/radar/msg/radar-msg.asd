
(cl:in-package :asdf)

(defsystem "radar-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "radar_message" :depends-on ("_package_radar_message"))
    (:file "_package_radar_message" :depends-on ("_package"))
  ))