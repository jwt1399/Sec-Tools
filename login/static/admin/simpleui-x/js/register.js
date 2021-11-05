if (parent.callback) {
    //如果是在子框架内就把首页刷新
    parent.callback();
}
var loginApp = new Vue({
    el: '.reg-main',
    data: {
        username: '',
        email: '',
        password: '',
        confirm_password: '',
        loading: false
    },
    methods: {
        register: function () {
            this.loading = true;
            if (this.username === "" || this.password === "") {
                this.$message.error("Please enter your username or password!");
                this.loading = false;
                return ;
            }elif(this.email === ""){
                this.$message.error("Please enter your email!");
                this.loading = false;
                return ;
            }elif(this.confirm_password === "" ){
                this.$message.error("Please enter the password again!");
                this.loading = false;
                return ;
            }elif(this.confirm_password != this.password){
                this.$message.error("Please enter the same password!");
                this.loading = false;
                return ;
            }
            this.$nextTick(function () {
                document.getElementById('reg-form').submit();
            });
        }
    }
});