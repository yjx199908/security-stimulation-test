rm -r target
mkdir target
zip ./target/app.zip *
mv ./target/app.zip ./target/app
chmod 755 ./target/app